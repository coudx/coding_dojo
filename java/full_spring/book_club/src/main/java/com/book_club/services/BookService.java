package com.book_club.services;

import com.book_club.models.Book;
import com.book_club.repos.BookRepo;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {

    private final BookRepo repo;

    public BookService(BookRepo repo) { this.repo = repo; }

    public List<Book> getAll() { return repo.getAll(); }

    public Book add(Book a) { return repo.save(a); }

    public Book find(Long id) { return repo.findById(id).orElse(null); }

    public Book update(Book a) { return repo.save(a); }
}
