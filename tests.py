import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture()
    def collector(self):
        return BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# проверяем, что метод set_book_genre корректно устанавливает жанр книге,
# если книга есть в словаре, а жанр — в списке допус
    def test_set_book_genre(self, collector):
        collector.add_new_book('Азазель')
        collector.set_book_genre('Азазель', 'Мультфильмы')

        assert collector.get_book_genre('Азазель') == 'Мультфильмы'

# проверяем, что метод set_book_genre вернет правильный жанр из установленной книги по названия
    def test_set_book_genre_return_correct_genre(self, collector):
        collector.add_new_book('Азазель')
        collector.set_book_genre('Азазель', 'Мультфильмы')

        assert collector.get_book_genre('Азазель') == 'Мультфильмы'


# проверяем, что метод get_books_with_specific_genre правильно выводит список книг с определенным жанром
    def test_get_books_with_specific_genre_returns_corrects_books(self, collector):
        collector.add_new_book('Азазель')
        collector.add_new_book('Капитан')
        collector.set_book_genre('Азазель', 'Мультфильмы')
        collector.set_book_genre('Капитан', 'Ужасы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Азазель']

# проверяем, что get_books_genre выводит словарь в правильном виде
    def test_get_books_genre_returns_correct_diction(self, collector):
        collector.add_new_book('Азазель')

        assert collector.get_books_genre() == {'Азазель': ''}

# Проверяем, что get_books_for_children возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга. Исключает книги с жанрами ужасы и тд
    def test_get_books_for_children_correct_age_rated_genres(self, collector):
        collector.add_new_book('Азазель')
        collector.add_new_book('Капитан')
        collector.set_book_genre('Азазель', 'Мультфильмы')
        collector.set_book_genre('Капитан', 'Ужасы')

        assert collector.get_books_for_children() == ['Азазель']

# Проверяем, add_book_in_favorites добавляет книгу в избранное, если она есть в book_genre
    def test_add_book_in_favorites_book_add(self, collector):
        collector.add_new_book('Азазель')
        collector.add_book_in_favorites('Азазель')

        assert collector.get_list_of_favorites_books() == ['Азазель']

# проверяем, delete_book_from_favorites удаляет книгу из избранного
    def test_delete_book_from_favorites_book_delete(self,collector):
        collector.add_new_book('Азазель')
        collector.add_book_in_favorites('Азазель')
        collector.delete_book_from_favorites('Азазель')

        assert collector.get_list_of_favorites_books() == []

#проверяем, get_list_of_favorites_books возвращает полный список книг из избранного
    def test_get_list_of_favorites_books_returns_correct_list(self,collector):
        collector.add_new_book('Азазель')
        collector.add_new_book('Капитан')
        collector.add_book_in_favorites('Азазель')
        collector.add_book_in_favorites('Капитан')

        assert collector.get_list_of_favorites_books() == ['Азазель', 'Капитан']

#граничные значения 40 символов добавляется в словарь add_new_book
    def test_add_new_book_name_length_40_symbols_add(self,collector):
        name = 'b' * 40
        collector.add_new_book(name)

        assert name in collector.get_books_genre()


#граничные значения 41 символов НЕ добавляется в словарь
    def test_add_new_book_name_length_41_symbols_add(self, collector):
        name = 'b' * 41
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()