from src.repositories.cards_repository import search_cards_by_name

def try_searching_cards_by_name(keyword):
    try:
        return search_cards_by_name(keyword)
    except Exception as e:
        print(f"Error searching cards: {e}")
        return []