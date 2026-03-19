def parse_optional_int(value: str, field_name: str):
    if not value:
        return None

    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{field_name}은(는) 숫자여야 합니다.")