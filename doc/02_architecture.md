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
