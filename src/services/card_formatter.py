def format_card(card):
    return_value = f"[{card['name_ko']}]\n종류: {card['card_kind']}\n"
    if card['card_kind'] == "몬스터":
        return_value += f"속성: {card['attribute']}\n종족: {card['race']}\n"
        return_value += "몬스터 종류:"
        if card['monster_type'] != "없음" and card['monster_type'] is not None:
            return_value += f"{card['monster_type']}"
        if card['is_effect'] == 1:
            return_value += " 효과"
        elif card['is_effect'] == 0:
            return_value += " 일반"
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
        return_value += " 몬스터 \n"
        if card['level'] is not None:
            return_value += f"레벨: {card['level']}\n"
        if card['rank'] is not None:
            return_value += f"랭크: {card['rank']}\n"
        if card['pendulum_scale'] is not None:
            return_value += f"펜듈럼 스케일: {card['pendulum_scale']}\n"
        if card['link_marker_count'] is not None and card['link_marker'] is not None:
            return_value += f"링크:({card['link_marker_count']}개)\n링크 마커 방향: "
            checker = card['link_marker']
            if checker & 1:
                return_value += " ↖"
            if checker & 2:
                return_value += " ↑"
            if checker & 4:
                return_value += " ↗"
            if checker & 8:
                return_value += " ←"
            if checker & 16:
                return_value += " →"
            if checker & 32:
                return_value += " ↙"
            if checker & 64:
                return_value += " ↓"
            if checker & 128:
                return_value += " ↘"
            return_value += "\n" 
        return_value += f"공격력: {card['atk']}\n"
        if card['defense'] is not None:
            return_value += f"수비력: {card['defense']}\n"
        if card['desc_ko']:
            return_value += f"텍스트: {card['desc_ko']}\n"
        if card['is_pendulum'] and card['pendulum_desc_ko']:
            return_value += f"펜듈럼 텍스트: {card['pendulum_desc_ko']}\n"
    elif card['card_kind'] == "마법":
        return_value += f"마법 카드 종류: {card['spell_type']}\n"
        if card['desc_ko']:
            return_value += f"텍스트: {card['desc_ko']}\n"
    elif card['card_kind'] == "함정":
        return_value += f"함정 카드 종류: {card['trap_type']}\n"
        if card['desc_ko']:
            return_value += f"텍스트: {card['desc_ko']}\n"

    return return_value