import unittest
from repositories.cite_repository import cite_repository
from logic.reference import Book, Article, Inproceedings


class TestCiteRepocitory(unittest.TestCase):
    def setUp(self):
        cite_repository.delete_all()

    def test_new_book(self):
        cite_repository.new_book(
            Book("Acronym", "Test Author", "Title", "2022", "Publisher"), "b{bikoodia"
        )
        books = cite_repository.get_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(
            [
                books[0].acronym,
                books[0].author,
                books[0].title,
                books[0].year,
                books[0].publisher,
                books[0].bibitex,
            ],
            ["Acronym", "Test Author", "Title", 2022, "Publisher", "b{bikoodia"],
        )

    def test_new_article(self):
        cite_repository.new_article(
            Article("Acronym", "Test Author", "Journal", "Title", "2020", "10", "10-12"),
            "b{bikoodia",
        )
        articles = cite_repository.get_articles()

        self.assertEqual(len(articles), 1)
        self.assertEqual(
            [
                articles[0].acronym,
                articles[0].author,
                articles[0].journal,
                articles[0].title,
                articles[0].year,
                articles[0].volume,
                articles[0].pages,
                articles[0].bibitex,
            ],
            ["Acronym", "Test Author", "Journal", "Title", 2020, 10, "10-12", "b{bikoodia"],
        )

    def test_new_inproceedings(self):
        cite_repository.new_inproceedings(
            Inproceedings("Acronym", "Test Author", "Title", "2022", "Booktitle"), "b{bikoodia"
        )
        inproceedings = cite_repository.get_inproceedings()

        self.assertEqual(len(inproceedings), 1)
        self.assertEqual(
            [
                inproceedings[0].acronym,
                inproceedings[0].author,
                inproceedings[0].title,
                inproceedings[0].year,
                inproceedings[0].booktitle,
                inproceedings[0].bibitex,
            ],
            ["Acronym", "Test Author", "Title", 2022, "Booktitle", "b{bikoodia"],
        )
        
    def test_get_bibitext(self):
        cite_repository.new_book(
            Book("Acronym", "Test Author", "Title", "2022", "Publisher"), "b{bikoodia"
        )
        books = cite_repository.get_bibitex("book")
        self.assertEqual([books[0].id, books[0].bibitex], [1, "b{bikoodia"])
    
    def test_get_bibitext_returs_empty_list_if_table_is_empty(self):
        books = cite_repository.get_bibitex("book")
        self.assertEqual(len(books), 0)

    def test_get_only_bibitext(self):
        cite_repository.new_book(
            Book("Acronym", "Test Author", "Title", "2022", "Publisher"), "b{bikoodia"
        )
        result = cite_repository.get_only_bibtex()
        self.assertEqual(result[0].bibitex, "b{bikoodia")
    
    def test_get_by_id(self):
        cite_repository.new_book(
            Book("Acronym", "Test Author", "Title", "2022", "Publisher"), "b{bikoodia"
        )
        cite_repository.new_inproceedings(
            Inproceedings("Acronym", "Test Author", "Title", "2022", "Booktitle"), "b{bikoodia"
        )
        result = cite_repository.get_by_id(2)
        print(result)
        self.assertEqual(result, 
                        (2,'Acronym', 'book', 'Title', 'Test Author', 2022, 'Publisher', None, None, None, None, 'b{bikoodia')
        )
