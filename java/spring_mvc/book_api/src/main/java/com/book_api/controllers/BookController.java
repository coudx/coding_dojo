package com.book_api.controllers;

import com.book_api.models.Book;
import com.book_api.services.BookService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
public class BookController {
    private final BookService bookService;
    public BookController(BookService bookService){
        this.bookService = bookService;
    }
    @RequestMapping("/books")
    public String index(Model model) {
        model.addAttribute("books", bookService.allBooks());
        return "index";
    }
    @RequestMapping("/books/{id}")
    public String show(@PathVariable("id") Long id, Model model) {
        Book book = bookService.findBook(id);
        model.addAttribute("book", book);
        return "show";
    }
}
