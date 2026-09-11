def validate_property(property):
    if (
        property["price"] > 0
        and property["suburb"] is not None
        and property["bedrooms"] >= 0
        and property["bathrooms"] > 0
        and property["land_size"] >= 0
    ):
        return True
    else:
        return False
