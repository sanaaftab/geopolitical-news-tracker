import pycountry

def validate_country_name(country_name):
    """
    Validate if the provided country name matches a real country.
    Returns True if valid, False otherwise.
    """
    try:
        pycountry.countries.search_fuzzy(country_name)[0]
        return True
    except:
        return False