from src.core.paths import SCHEMA_PATH
from src.db.connection import get_db_connection, close_db_connection


def init_db():
    conn = get_db_connection()

    if conn is None:
        print("데이터베이스 초기화에 실패했습니다.: 연결 오류")
        return

    try:
        schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema_sql)
        conn.commit()
        print("데이터베이스가 성공적으로 초기화되었습니다.")
    except Exception as e:
        print(f"데이터베이스 초기화 중 오류가 발생했습니다: {e}")
    finally:
        close_db_connection(conn)