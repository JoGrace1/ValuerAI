from utils.filter_properties import filter_properties
from data.properties import properties

filtered = filter_properties(
    properties,
    min_bedrooms=3,
    wanted_suburb="Newtown",
    min_land_size=400
)

print(filtered)
