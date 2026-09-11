from utils.filter_properties import filter_properties
from utils.validate_property import validate_property
from utils.get_prices import get_prices
import json

valid_properties = []
json_properties = []
with open("app/data/properties.json", "r") as file:
    json_properties = json.load(file)
    print("DATA ", json_properties)

for property in json_properties:
    if validate_property(property):
        valid_properties.append(property)
filtered = filter_properties(
    valid_properties,
    min_bedrooms=3,
    wanted_suburb="Newtown",
    min_land_size=400
)
price_list = get_prices(filtered)



with open("app/data/properties.json", "r") as file:
    data = json.load(file)
    data2 = json.loads(json.dumps(data))
    print("DATA loads ", data2)

print(len(properties))
print(len(valid_properties))
print(len(filtered))
print(filtered)
print(valid_properties)
