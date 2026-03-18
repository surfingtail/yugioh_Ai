from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent

DATA_DIR = ROOT_DIR / "data"
DB_DIR = DATA_DIR / "db"
SQL_DIR = ROOT_DIR / "sql"

DB_PATH = DB_DIR / "yugioh.db"
SCHEMA_PATH = SQL_DIR / "schema.sql"