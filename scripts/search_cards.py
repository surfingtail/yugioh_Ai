from src.repositories.cards_repository import search_cards_by_name
from src.services.card_formatter import format_card

if __name__ == "__main__":
    keyword = input("Enter a keyword to search for cards: ")
    results = search_cards_by_name(keyword)
    if results:
        for card in results:
            print(format_card(card))
            print("-" * 40)
    else:
            print("No cards found matching the keyword.")