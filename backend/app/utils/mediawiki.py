import requests

API_URL = 'https://bulbapedia.bulbagarden.net/w/api.php'

def fetch_route_page(region: str, route_id: str) -> str:
    page_title = f"{region.title()}_{route_id.replace(' ', '_').title()}"

    sections_resp = requests.get(API_URL, params={
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "sections"
    }).json()
    
    if "error" in sections_resp:
        raise ValueError("Route not found!")

    sections = sections_resp["parse"]["sections"]

    pokemon_section_index = None
    for section in sections:
        if section["line"] == "Pokémon":
            pokemon_section_index = section["index"]
            break

    if pokemon_section_index is None:
        raise ValueError("Pokémon section not found")

    html = requests.get(API_URL, params={
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "text",
        "section": pokemon_section_index
    }).json()["parse"]["text"]["*"]

    return html