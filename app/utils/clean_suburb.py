def clean_suburb(property, error):
    try: 
        suburb = property["suburb"]
        if suburb is None:
            error.append({
                "property_id": property["id"],
                "error": "Suburb is None"
            })
            return None
        elif not isinstance(suburb, str):
            try:
                suburb = str(suburb)
                property["suburb"] = suburb
            except ValueError:
                error.append({
                    "property_id": property["id"],
                    "error": "Suburb is not a string"
                })
                return None
       
    except KeyError:
        error.append({
            "property_id": property["id"],
            "error": "Suburb key is missing"
        })
        property["suburb"] = ""
    
    return property