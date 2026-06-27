# Архитектура v1 (эволюционная)

## Целевая схема (к которой идём)
```mermaid
flowchart LR
  U[User/Browser] -->|HTTP| DJ[Django web-api]
  DJ -->|HTTP| SS[FastAPI search-service]
  SS --> R[(Redis)]
  SS --> PG[(PostgreSQL)]
  SS --> C1[collector-wb]
  SS --> C2[collector-ozon]
  SS --> C3[collector-ym]
  C1 --> EXT1[WB]
  C2 --> EXT2[Ozon]
  C3 --> EXT3[Yandex Market]


flowchart LR
  U[User/Browser] --> DJ[Django + DRF]
  DJ --> SS[FastAPI search-service]
  SS --> R[(Redis)]
  DJ --> PG[(PostgreSQL)]
  SS --> PG


sequenceDiagram
  actor User
  participant DJ as Django web-api
  participant SS as search-service
  participant R as Redis
  participant PG as PostgreSQL
  participant COL as collector

  User->>DJ: GET /search?q=...
  DJ->>SS: GET /api/search?q=...
  SS->>R: GET cache(search:q)
  alt cache hit
    SS-->>DJ: results
  else cache miss
    SS->>COL: fetch offers(q)
    COL-->>SS: offers
    SS->>PG: upsert offers
    SS->>R: SET cache(search:q) TTL
    SS-->>DJ: results
  end
  DJ-->>User: HTML/JSON
