from src.core.paths import DB_PATH
from src.db.init_db import init_db

import os


def reset_db():

    if DB_PATH.exists():
        os.remove(DB_PATH)
        print("기존 데이터베이스 파일이 삭제되었습니다.")

    init_db()

if __name__ == "__main__":
    reset_db()