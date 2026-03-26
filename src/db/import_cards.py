from src.db.connection import get_db_connection, close_db_connection
from src.utils.json_utils import read_json
from src.core.paths import DATA_DIR


def import_cards():
    conn = get_db_connection()

    if conn is None:
        print("데이터베이스 연결에 실패했습니다: 연결 오류")
        return

    try:
        cards = read_json(DATA_DIR / "normalized/cards.sample.json")

        for card in cards:
            conn.execute("""
                INSERT OR IGNORE INTO cards (
                    card_id,
                    name_ko,
                    desc_ko,
                    pendulum_desc_ko,
                    card_kind,
                    spell_type,
                    trap_type,
                    is_effect,
                    monster_type,
                    is_pendulum,
                    attribute,
                    race,
                    is_tuner,
                    is_special_summon,
                    is_flip,
                    is_toon,
                    is_spirit,
                    is_union,
                    is_gemini,
                    level,
                    rank,
                    pendulum_scale,
                    link_marker_count,
                    link_marker,
                    atk,
                    defense,
                    is_official_translation
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                card.get("card_id"),
                card.get("name_ko"),
                card.get("desc_ko"),
                card.get("pendulum_desc_ko"),
                card.get("card_kind"),
                card.get("spell_type"),
                card.get("trap_type"),
                card.get("is_effect"),
                card.get("monster_type"),
                card.get("is_pendulum"),
                card.get("attribute"),
                card.get("race"),
                card.get("is_tuner"),
                card.get("is_special_summon"),
                card.get("is_flip"),
                card.get("is_toon"),
                card.get("is_spirit"),
                card.get("is_union"),
                card.get("is_gemini"),
                card.get("level"),
                card.get("rank"),
                card.get("pendulum_scale"),
                card.get("link_marker_count"),
                card.get("link_marker"),
                card.get("atk"),
                card.get("defense"),
                card.get("is_official_translation"),
            ))

        conn.commit()
        print("카드들이 성공적으로 가져와졌습니다.")

    except Exception as e:
        print(f"카드 가져오기 중 오류가 발생했습니다: {e}")

    finally:
        close_db_connection(conn)