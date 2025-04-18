import requests
from api_chitaigorod import ChitaiGorodAPI


url = ChitaiGorodAPI("https://web-gate.chitai-gorod.ru/api/v2search/product")


def test_search_book_name_positive():
    title = "маугли"
    result = url.serch_product(phrase=title)
    assert result.status_code == 200
