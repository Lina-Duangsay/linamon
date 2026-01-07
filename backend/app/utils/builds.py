
# builds the bulbapedia URL using parameters 
url = 'https://bulbapedia.bulbagarden.net/wiki'

def build_bulbapedia_url(region: str, route_id: str) -> str:
    region = region.title()
    route_name = route_id.replace(" ", "_").title()
    return f"{url}/{region}_{route_name}"