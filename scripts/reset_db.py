from src.core.paths import DB_PATH
from src.db.init_db import init_db

import os


def reset_db():

    if DB_PATH.exists():
        os.remove(DB_PATH)
        print("Old database removed")

    init_db()

if __name__ == "__main__":
    reset_db()
    reset_db()