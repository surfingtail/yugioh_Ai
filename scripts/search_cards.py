from src.repositories.cards_repository import search_cards
from src.services.card_formatter import format_card
from src.services.int_parser import parse_optional_int

if __name__ == "__main__":

    filters = {}
    try:
        name = input("카드 이름:").strip()
        if name:
            filters["name"] = name
        card_kind = input("카드 종류 (Monster, Spell, Trap):").strip()
        if card_kind:
            filters["card_kind"] = card_kind
        min_atk = input("최소 공격력:").strip()
        if min_atk:
            filters["min_atk"] = parse_optional_int(min_atk, "최소 공격력")
        max_atk = input("최대 공격력:").strip()
        if max_atk:
            filters["max_atk"] = parse_optional_int(max_atk, "최대 공격력")
        min_defense = input("최소 수비력:").strip()
        if min_defense:
            filters["min_defense"] = parse_optional_int(min_defense, "최소 수비력")
        max_defense = input("최대 수비력:").strip()
        if max_defense:
            filters["max_defense"] = parse_optional_int(max_defense, "최대 수비력")

    except Exception as e:
        print(f"입력 형식이 잘못되었습니다: {e}")
        raise SystemExit

    cards = search_cards(filters)

    if not cards:
        print("검색된 카드가 없습니다.")
    else:
        for card in cards:
            print(format_card(card))
            print("-" * 40)