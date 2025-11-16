class Book:
    """
    Данный класс описывает книгу.
    """

    def __init__(self, title: str = "",
                 author: str = "", pages: int = 0) -> None:
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.
        """
        self._title = title
        self._author = author
        self._pages = pages

    def get_title(self) -> str:
        """
        Получить название книги.

        :return: Название книги.
        """
        return self._title

    def get_author(self) -> str:
        """
        Получить автора книги.

        :return: Автор книги.
        """
        return self._author

    def get_pages(self) -> int:
        """
        Получить количество страниц.

        :return: Количество страниц.
        """
        return self._pages

    def set_title(self, title: str) -> None:
        """
        Установить название книги.

        :param title: Новое название книги.
        """
        self._title = title

    def set_author(self, author: str) -> None:
        """
        Установить автора книги.

        :param author: Новый автор книги.
        """
        self._author = author

    def set_pages(self, pages: int) -> None:
        """
        Установить количество страниц.

        :param pages: Новое количество страниц.
        """
        if pages > 0:
            self._pages = pages

    def display_info(self) -> str:
        """
        Показать информацию о книге.

        :return: Информация о книге.
        """
        return f'Книга: "{self._title}", Автор: {self._author}, Количество страниц: {self._pages}'

    def is_fat_book(self) -> bool:
        """
        Проверить, является ли книга толстой.

        :return: True если страниц больше 500.
        """
        return self._pages > 500

    def get_reading_time(self, pages_per_hour: int = 50) -> float:
        """
        Рассчитать примерное время чтения книги.

        :param pages_per_hour: Страниц в час.
        :return: Время чтения в часах.
        """
        return self._pages / pages_per_hour


class BookManager:
    """
    Менеджер для работы с книгами.
    """

    def __init__(self) -> None:
        """
        Инициализация менеджера книг.
        """
        self.books = []

    def add_book(self, book: Book) -> None:
        """
        Добавить книгу в коллекцию.

        :param book: Книга для добавления.
        """
        self.books.append(book)

    def show_all_books(self) -> None:
        """
        Показать все книги в коллекции.
        """
        print("\nВсе книги в коллекции:")
        for book in self.books:
            print('+', book.display_info())


class main:
    """
    Основной класс программы.
    """
    
    def __init__(self) -> None:
        """
        Инициализация основной логики программы.
        """
        self.manager = BookManager()
        self._run_program()

    def _run_program(self) -> None:
        """
        Запуск основной логики программы.
        """
        book1 = Book("Преступление и наказание", "Фёдор Достоевский", 672)
        book2 = Book()
        book2.set_title("Мастер и Маргарита")
        book2.set_author("Михаил Булгаков")
        book2.set_pages(480)

        self.manager.add_book(book1)
        self.manager.add_book(book2)

        self.manager.show_all_books()

        print("\nДемонстрация")
        
        print(f"\nИнформация о книге 1:\n{book1.display_info()}")
        print(f"Толстая ли книга? {book1.is_fat_book()}")
        print(f"Время чтения: {book1.get_reading_time()} часов")

        print(f"\nИнформация о книге 2:\n{book2.display_info()}")
        print(f"Толстая ли книга? {book2.is_fat_book()}")
        print(f"Время чтения: {book2.get_reading_time()} часов")

        program_running = True
        while program_running:
            print("\n" + "=" * 23)
            print("МЕНЮ УПРАВЛЕНИЯ КНИГАМИ")
            print("=" * 23)
            print("1. Добавить новую книгу")
            print("2. Выйти из программы")
            
            choice = input("Выберите действие (1-2): ")
            
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                pages = int(input("Введите количество страниц: "))
                new_book = Book(title, author, pages)
                self.manager.add_book(new_book)
                self.manager.show_all_books()
            
            elif choice == "2":
                program_running = False
            
            else:
                print("Неверный выбор")

main()