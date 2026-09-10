suburbs = ["Newtown", "Surry Hills", "Glebe", "Waterloo"]
def filter_properties(properties, min_bedrooms, wanted_suburb, min_land_size):
    filtered_properties = []
    for property in properties:
        if property["bedrooms"] >= min_bedrooms and property["suburb"] == wanted_suburb and property["land_size"] >= min_land_size:
            filtered_properties.append(property)
    return filtered_properties
