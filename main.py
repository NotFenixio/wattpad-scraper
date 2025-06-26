import requests
from core.epub_exporter import export_to_epub
from core.extractor import extract_book_info, recursively_extract_chapter_content

def get_book(id: int) -> dict:
    """Fetch a book from Wattpad using its ID.
    Args:
        id (int): The ID of the book to fetch.
    Returns:
        dict: The book data.
    """
    url: str = f"https://www.wattpad.com/story/{id}?language=5" # Language 5 is English
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    })

    if response.status_code != 200:
        raise Exception(f"Failed to fetch book with ID {id}: {response.status_code}")
    
    return response.content

def run(book_id: int):
    """
    runs the whole party thingaroo and exports a book to epub
    """

    book_data = extract_book_info(get_book(book_id))
    chapters = recursively_extract_chapter_content(book_data)
    book_data['chapters'] = chapters
    export_to_epub(book_data, "output/book.epub")
    print(f"Book '{book_data['title']}' by {book_data['author']} has been exported to 'output/book.epub'.")