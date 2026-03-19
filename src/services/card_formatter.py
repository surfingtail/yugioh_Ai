def format_card(card):
    return_value = f"[{card['name_ko']}]\n종류: {card['card_kind']}\n"
    if card['card_kind'] == "Monster":
        return_value += f"속성: {card['attribute']}\n종족: {card['race']}\n"
        return_value += f"몬스터 타입: {card['monster_type']}"
        if card['is_pendulum']:
            return_value += " 펜듈럼"
        if card['is_tuner']:
            return_value += " 튜너"
        if card['is_special_summon']:
            return_value += " 특수 소환"
        if card['is_flip']:
            return_value += " 리버스"
        if card['is_toon']:
            return_value += " 툰"
        if card['is_spirit']:
            return_value += " 스피릿"
        if card['is_union']:
            return_value += " 유니온"
        if card['is_gemini']:
            return_value += " 듀얼"
        return_value += "몬스터 \n"
        if card['level']:
            return_value += f"레벨: {card['level']}\n"
        if card['rank']:
            return_value += f"랭크: {card['rank']}\n"
        if card['pendulum_scale']:
            return_value += f"펜듈럼 스케일: {card['pendulum_scale']}\n"
        if card['link_marker_count'] and card['link_marker']:
            return_value += f"링크 마커:({card['link_marker_count']}개)\n링크 마커 방향: "
            checker = card['link_marker']
            if checker & 1:
                return_value += "↖"
            if checker & 2:
                return_value += "↑"
            if checker & 4:
                return_value += "↗"
            if checker & 8:
                return_value += "←"
            if checker & 16:
                return_value += "→"
            if checker & 32:
                return_value += "↙"
            if checker & 64:
                return_value += "↓"
            if checker & 128:
                return_value += "↘"
            return_value += "\n" 
        return_value += f"공격력: {card['atk']}\n"
        if card['defense'] is not None:
            return_value += f"수비력: {card['defense']}\n"
        return_value += f"텍스트: {card['desc_ko']}\n"
        if card['is_pendulum']:
            return_value += f"펜듈럼 텍스트: {card['pendulum_desc_ko']}\n"
    elif card['card_kind'] == "Spell":
        return_value += f"마법 카드 타입: {card['spell_type']}\n"
        return_value += f"텍스트: {card['desc_ko']}\n"
    elif card['card_kind'] == "Trap":
        return_value += f"함정 카드 타입: {card['trap_type']}\n"
        return_value += f"텍스트: {card['desc_ko']}\n"

    return return_value