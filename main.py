import os
import requests
import functions_framework
from flask import jsonify
from dotenv import load_dotenv

load_dotenv()

class StarWarsService:
    BASE_URL = "https://swapi.dev/api"

    @classmethod
    def fetch_data(cls, resource, params=None):
        """
        Realiza a requisição HTTP principal para a API externa.
        Inclui tratamento de exceções robusto e timeout para evitar travamentos.
        """
        try:
            response = requests.get(f"{cls.BASE_URL}/{resource}/", params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": "Falha na comunicação com a SWAPI", "details": str(e), "code": 502}

    @classmethod
    def get_related_names(cls, url_list):
        """
            Resolve URLs correlacionadas para nomes amigáveis.
        """
        names = []
        for url in url_list[:5]: # Limitado a 5 para manter a performance
            try:
                res = requests.get(url, timeout=5)
                if res.status_code == 200:
                    names.append(res.json().get('name') or res.json().get('title'))
            except:
                continue
        return names

@functions_framework.http
def hello_http(request):
    # 1. Autenticação
    expected_api_key = os.getenv('API_KEY')
    api_key = request.headers.get('x-api-key')
    if not api_key or api_key != expected_api_key:
        return jsonify({"error": "Autenticação necessária ou chave inválida."}), 401

    # 2. Captura de Parâmetros
    resource = request.args.get('resource', 'people')
    search = request.args.get('search')
    sort_by = request.args.get('sort_by')
    expand = request.args.get('expand', 'false').lower() == 'true'

    # 3. Validação de Recursos
    valid_resources = ['people', 'planets', 'starships', 'films', 'species', 'vehicles']
    if resource not in valid_resources:
        return jsonify({"error": f"Recurso '{resource}' inválido."}), 400

    # 4. Execução da Consulta
    params = {'search': search} if search else {}
    data = StarWarsService.fetch_data(resource, params)

    if "error" in data:
        return jsonify(data), data.get("code", 500)

    results = data.get('results', [])

    # 5. Complexidade Extra: Dados Correlacionados (Expandir nomes)
    if expand and resource == 'films' and results:
        for film in results:
            film['character_names'] = StarWarsService.get_related_names(film.get('characters', []))

    # 6. Complexidade Extra: Ordenação Dinâmica
    if sort_by and results:
        try:
            # Tenta converter para float/int para ordenação numérica, 
            # se falhar (ex: ordenar por nome), mantém como string.
            results.sort(key=lambda x: float(x.get(sort_by)) if x.get(sort_by, "").isdigit() else x.get(sort_by, ""))
        except Exception:
            pass

    return jsonify({
        "status": "success",
        "resource_queried": resource,
        "total_on_page": len(results),
        "data": results
    }), 200