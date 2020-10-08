
def format_places(city_name, country_name, population):
    return f"{city_name}, {country_name} - {population}"


def format_places_optional(city_name, country_name, population=None):
    if population == None: return f"{city_name}, {country_name}"
    return f"{city_name}, {country_name} - {population}"

