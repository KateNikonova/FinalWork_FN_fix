import pytest
from pages.api_chitaigorod import ChitaiGorodAPI
from config import API_URL


url = ChitaiGorodAPI(API_URL)

@pytest.mark.parametrize("title", [
    "маугли",
    "джоан роулинг",
    "1984",
    "война и мир"
])
def test_search_book_name_positive(title):
    result = url.search_product(phrase=title)
    assert result.status_code == 200
    assert result.json()["data"]["attributes"]["transformedPhrase"] == title
