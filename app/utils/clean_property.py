from utils.clean_price import clean_price
from utils.clean_bedrooms import clean_bedrooms
from utils.clean_suburb import clean_suburb

def clean_property(properties, error):
    clean_properties = []
    for property in properties:
        cleaned_price = clean_price(property, error)
        cleaned_bedrooms = clean_bedrooms(property, error)
        cleaned_suburb = clean_suburb(property, error)

        if cleaned_price is None:
            print(f"Property {property['id']} is invalid.")
            continue

        if cleaned_bedrooms is None:
            continue

        if cleaned_suburb is None:
            continue

        clean_properties.append(property)
    print(f"Valid properties: {len(clean_properties)}")
    return clean_properties