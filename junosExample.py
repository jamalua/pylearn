import json
from pprint import pprint

with open("jun_show_route.json") as f:
    route_data = json.load(f)

pprint(route_data)

for route_table in route_data["route-information"][0]["route-table"]:
    print(route_table["table-name"][0]["data"])

print("-" * 30)

