from src.db.connection import get_db_connection, close_db_connection

def search_cards(filters):
    conn = get_db_connection()

    try:
        query = "SELECT card_id, name_ko, desc_ko, pendulum_desc_ko, card_kind, spell_type, trap_type, monster_type, is_pendulum, attribute, race, is_tuner, is_special_summon, is_flip, is_toon, is_spirit, is_union, is_gemini, level, rank, pendulum_scale, link_marker_count, link_marker, atk, defense, is_official_translation FROM cards WHERE 1=1"
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
                "desc_ko": row[2],
                "pendulum_desc_ko": row[3],
                "card_kind": row[4],
                "spell_type": row[5],
                "trap_type": row[6],
                "monster_type": row[7],
                "is_pendulum": row[8],
                "attribute": row[9],
                "race": row[10],
                "is_tuner": row[11],
                "is_special_summon": row[12],
                "is_flip": row[13],
                "is_toon": row[14],
                "is_spirit": row[15],
                "is_union": row[16],
                "is_gemini": row[17],
                "level": row[18],
                "rank": row[19],
                "pendulum_scale": row[20],
                "link_marker_count": row[21],
                "link_marker": row[22],
                "atk": row[23],
                "defense": row[24],
                "is_official_translation": row[25]
            }
            for row in rows
        ]

        return card_data


    except Exception:
        return []
    
    finally:
        close_db_connection(conn)
    