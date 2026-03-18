from src.db.connection import get_db_connection, close_db_connection


def search_cards_by_name(keyword):
    conn = get_db_connection()

    if conn is None:
        print("DB connection failed")
        return []

    try:
        cursor = conn.execute(
            """
            SELECT card_id, name_ko, card_kind, atk, defense
            FROM cards
            WHERE name_ko LIKE ?
            """,
            (f"%{keyword}%",)
        )

        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print(f"Error searching cards: {e}")
        return []

    finally:
        close_db_connection(conn)