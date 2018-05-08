#!/usr/bin/env python

try:
    import requests
    from time import strftime
except ImportError:
    # Python 2
    raise ImportError


query = """[out:xml][timeout:160];(node(user:"rivermont");way(user:"rivermont");relation(user:"rivermont"););out meta;>;out meta qt;"""

time = strftime("%b_%d_%Y_%H-%M")
outfile = "{0}.osm".format(time)

print("Retrieving data from server...")
response = requests.get("http://overpass-api.de/api/interpreter?data={0}".format(query))

print("Writing data to {0}".format(outfile))
with open(outfile, "wb+") as f:
    f.write(response.content)

print("Done.")

