properties = [
    {
        "address": "123 Example Street",
        "suburb": "Newtown",
        "price": 850000,
        "bedrooms": 3,
        "bathrooms": 2,
        "land_size": 450
    },
    {
        "address": "45 King Street",
        "suburb": "Glebe",
        "price": 920000,
        "bedrooms": 4,
        "bathrooms": 2,
        "land_size": 500
    },
    {
        "address": "8 Park Road",
        "suburb": "Newtown",
        "price": 760000,
        "bedrooms": 2,
        "bathrooms": 1,
        "land_size": 300
    },
    {
        "address": "18 Park Road",
        "suburb": "Newtown",
        "price": 1050000,
        "bedrooms": 3,
        "bathrooms": 2,
        "land_size": 410
    }
]

suburbs = ["Newtown", "Surry Hills", "Glebe", "Waterloo"]
def filter_properties(properties, min_bedrooms, wanted_suburb, min_land_size):
    filtered_properties = []
    for property in properties:
        if property["bedrooms"] >= min_bedrooms and property["suburb"] == wanted_suburb and property["land_size"] >= min_land_size:
            filtered_properties.append(property)
    return filtered_properties
filtered_properties =filter_properties(properties, min_bedrooms=3, wanted_suburb="Newtown", min_land_size=400)
print(filtered_properties)
print(f"{properties[0]['address']} in {properties[0]['suburb']} costs {properties[0]['price']} AUD has {properties[0]['bedrooms']} bedrooms {properties[0]['bathrooms']} bathrooms and {properties[0]['land_size']} sqm of land.")
