from src.db.connection import get_db_connection, close_db_connection

def search_cards(filters):
    conn = get_db_connection()

    try:
        query = "SELECT card_id, name_ko, card_kind, atk, defense FROM cards WHERE 1=1"
        params = []

        if filters.get("name"):
            query += " AND name_ko LIKE ?"
            params.append(f"%{filters['name']}%")

        if filters.get("card_kind"):
            query += " AND card_kind = ?"
            params.append(filters["card_kind"])

        if filters.get("min_atk") is not None:
            query += " AND atk >= ?"
            params.append(filters["min_atk"])

        if filters.get("max_atk") is not None:
            query += " AND atk <= ?"
            params.append(filters["max_atk"])

        if filters.get("min_defense") is not None:
            query += " AND defense >= ?"
            params.append(filters["min_defense"])
        
        if filters.get("max_defense") is not None:
            query += " AND defense <= ?"
            params.append(filters["max_defense"])
        
        cursor = conn.execute(query, params)
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


    except Exception:
        return []
    
    finally:
        close_db_connection(conn)
    