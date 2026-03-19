from src.repositories.cards_repository import search_cards
from src.services.card_formatter import format_card

if __name__ == "__main__":

    filters = {}
    try:
        name = input("카드 이름:")
        if name:
            filters["name"] = name

        card_kind = input("카드 종류 (Monster, Spell, Trap):")
        if card_kind:
            filters["card_kind"] = card_kind
        min_atk = input("최소 공격력:")
        if min_atk:
            try:
                filters["min_atk"] = int(min_atk)
            except:
                if min_atk == "":
                    min_atk = None
                else:
                    raise ValueError("최소 공격력은 숫자여야 합니다.")
        max_atk = input("최대 공격력:")
        if max_atk:
            try:
                filters["max_atk"] = int(max_atk)
            except:
                if max_atk == "":
                    max_atk = None
                else:
                    raise ValueError("최대 공격력은 숫자여야 합니다.")
        min_defense = input("최소 수비력:")
        if min_defense:
            try:
                filters["min_defense"] = int(min_defense)
            except:
                if min_defense == "":
                    min_defense = None
                else:
                    raise ValueError("최소 수비력은 숫자여야 합니다.")
        max_defense = input("최대 수비력:")
        if max_defense:
            try:
                filters["max_defense"] = int(max_defense)
            except:
                if max_defense == "":
                    max_defense = None
                else:
                    raise ValueError("최대 수비력은 숫자여야 합니다.")

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