from src.db.connection import get_db_connection, close_db_connection

def search_cards_by_name(keyword):
    conn = get_db_connection()

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

        card_data = [
            {
                "card_id": row[0],
                "name_ko": row[1],
                "card_kind": row[2],
                "atk": row[3],
                "defense": row[4]
            }
            for row in rows
        ]

        return card_data
    
    except Exception as e:
        print(f"Error searching cards: {e}")
        return []
    
    finally:
        close_db_connection(conn)