package com.book_api.services;
// ...
import com.book_api.models.Book;
import com.book_api.repos.BookRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class BookService {
    // adding the book repository as a dependency
    private final BookRepository bookRepository;

    public BookService(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
    // returns all the books
    public List<Book> allBooks() {
        return bookRepository.findAll();
    }
    // creates a book
    public Book createBook(Book b) {
        return bookRepository.save(b);
    }
    // retrieves a book
    public Book findBook(Long id) {
        Optional<Book> optionalBook = bookRepository.findById(id);
        return optionalBook.orElse(null);
    }

    public Book updateBook(Long id, String title, String desc, String lang, Integer numOfPages) {
        return bookRepository.save(new Book(id,title,desc,lang,numOfPages));
    }

    public void deleteBook(Long id) {
        bookRepository.deleteById(id);
    }
}

