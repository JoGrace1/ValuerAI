from utils.filter_properties import filter_properties
from data.properties import properties
from utils.validate_property import validate_property
valid_properties = []
for property in properties:
    if validate_property(property):
        valid_properties.append(property)
filtered = filter_properties(
    valid_properties,
    min_bedrooms=3,
    wanted_suburb="Newtown",
    min_land_size=400
)
print(len(properties))
print(len(valid_properties))
print(len(filtered))
print(filtered)
print(valid_properties)
