def format_card(card):
    return f"""[{card['name_ko']}]
ID: {card['card_id']}
종류: {card['card_kind']}
ATK: {card['atk']}
DEF: {card['defense']}"""
