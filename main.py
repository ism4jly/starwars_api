import requests
import functions_framework
from flask import jsonify

@functions_framework.http
def hello_http(request):
    resource = request.args.get('resource', 'people')
    search_term = request.args.get('search')

    valid_resources = ['people', 'planets', 'starships', 'films', 'species', 'vehicles']
    if resource not in valid_resources:
        return jsonify({"error": f"Recurso '{resource}' inválido."}), 400

    swapi_url = f"https://swapi.dev/api/{resource}/"
    params = {'search': search_term} if search_term else {}

    try:
        response = requests.get(swapi_url, params=params, timeout=10)
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erro ao acessar a API Star Wars", "details": str(e)}), 502