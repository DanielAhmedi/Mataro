```mermaid
flowchart LR
  U[User/Browser] --> DJ[Django + DRF]
  DJ --> SS[FastAPI search-service]
  SS --> R[(Redis)]
  DJ --> PG[(PostgreSQL)]
  SS --> PG
