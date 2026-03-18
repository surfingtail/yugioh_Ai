from src.db.search_cards import search_cards_by_name

if __name__ == "__main__":
    keyword = input("검색할 카드 이름을 입력하세요: ")
    results = search_cards_by_name(keyword)

    print(f"검색 결과: {results}")