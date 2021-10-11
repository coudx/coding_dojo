package com.pokebook.services;

// ...
import com.pokebook.models.Pokebook;
import com.pokebook.repos.PokebookRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PokebookService {
    // adding the book repository as a dependency
    private final PokebookRepository bookRepository;

    public PokebookService(PokebookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
    // returns all the books
    public List<Pokebook> allBooks() {
        return bookRepository.findAll();
    }
    // creates a book
    public Pokebook createBook(Pokebook b) {
        return bookRepository.save(b);
    }
    // retrieves a book
    public Pokebook findBook(Long id) {
        Optional<Pokebook> optionalBook = bookRepository.findById(id);
        return optionalBook.orElse(null);
    }

    public Pokebook updateBook(Pokebook poke) {
        return bookRepository.save(poke);
    }
}


