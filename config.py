import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_part_1_user:qmjLnQ3yHtoxl8WwdiczWW9gC0qpAAnd@dpg-cqvla0tds78s739m24bg-a.oregon-postgres.render.com/sit722_part_1")

settings = Settings()