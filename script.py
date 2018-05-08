import requests

query = """[out:xml][timeout:160];(node(user:"rivermont");way(user:"rivermont");relation(user:"rivermont"););out meta;>;out meta qt;"""

response = requests.get("http://overpass-api.de/api/interpreter?data={0}".format(query))

with open ("data.osm", "w+") as f:
    f.write(response.text)
