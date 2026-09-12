def clean_bedrooms(property, error):
    try:
        bedroom = property["bedrooms"]
        if bedroom is None:
            error.append({
                "property_id": property["id"],
                "error": "Bedrooms is None"
            })
            return None
        
        elif not isinstance(bedroom, int):
            try: 
                bedroom = int(bedroom)
                property["bedrooms"] = bedroom
            except ValueError:
                error.append({
                    "property_id": property["id"],
                    "error": "Bedrooms is not a number"
                })
                return None
    except KeyError:
        error.append({
            "property_id": property["id"],
            "error": "Bedrooms key is missing"
        })
        property["bedrooms"] = 0

    return property 