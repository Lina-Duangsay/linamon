from bs4 import BeautifulSoup
from app.utils.mediawiki import fetch_route_page


def parsePokemon(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    
    table = soup.find("table", class_= "roundy")
    if not table:
        return []
    
    pokemon = []

    rows = table.find_all("tr")[1:] 
    for row in rows:
        cells = row.find_all("td")
        if len(cells) <= 5:
            continue

        name_tag = cells[1].select_one("a[href^='/wiki/']")
        name = name_tag.text.strip() if name_tag else None

        location = cells[2].get_text(strip=True)
        levels = cells[5].get_text(strip=True)
        rate = cells[-1].get_text(strip=True)

        pokemon.append({
            "name": name,
            "location": location,
            "levels": levels,
            "rate": rate
        })

    return pokemon