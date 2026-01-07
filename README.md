# Linamon

Linamon is a Python-based REST API that retrieves and returns Pokémon encounter data by region and route.  
It integrates with the Bulbapedia MediaWiki API, parses route data, and exposes clean, structured JSON responses via FastAPI.

This project demonstrates backend API design, third‑party API integration, HTML parsing, and error handling.

## Features

- RESTful API built with **FastAPI**
- Retrieves Pokémon encounter data by **region** and **route**
- Integrates with the **MediaWiki API**
- Parses HTML content using **BeautifulSoup**
- Returns normalized, structured **JSON responses**
- Graceful error handling for invalid routes or regions

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **HTTP Requests:** Requests
- **Parsing:** BeautifulSoup
- **API Source:** Bulbapedia MediaWiki API

## API Usage

### Endpoint
GET /routes/{region}/{route}

http://127.0.0.1:8000/routes/kalos/route_9


### Example Response

```json
{
  "region": "kalos",
  "route": "route_9",
  "pokemon": [
    {
      "name": "Mightyena",
      "location": "Grass",
      "levels": "34-36",
      "rate": "30%"
    },
    {
      "name": "Skorupi",
      "location": "Grass",
      "levels": "34-35",
      "rate": "20%"
    }
  ]
}
