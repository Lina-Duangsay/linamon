from fastapi import FastAPI, HTTPException
from app.utils.mediawiki import fetch_route_page
from app.utils.soup import parsePokemon
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sylviemon Route Guide")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/routes/{region}/{route_id}")
async def get_pokemon_on_route(region: str, route_id: str):
    try:
        html = fetch_route_page(region, route_id)
        pokemon = parsePokemon(html)
        
        return {
            "region": region.title(),
            "route": route_id.title(),
            "pokemon" : pokemon
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
