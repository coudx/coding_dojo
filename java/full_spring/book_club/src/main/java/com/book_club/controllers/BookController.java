package com.book_club.controllers;

import com.book_club.models.Book;
import com.book_club.services.BookService;
import com.book_club.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

@Controller
@RequestMapping("books")
public class BookController {

    @Autowired
    private BookService service;
    @Autowired
    private UserService userServ;

    @GetMapping
    public String books(Model model, HttpSession session) {
        Long uid = (Long) session.getAttribute("user_id");
        model.addAttribute("user", userServ.readUserData(uid));
        model.addAttribute("books", service.getAll());
        return "books/index";
    }

    @PostMapping("new")
    public String add(@Valid @ModelAttribute("book") Book book, BindingResult result, Model model) {
        if (result.hasErrors()) {
            return "redirect:new";
        }
        service.add(book);
        return "redirect:" + book.getId();
    }

    @GetMapping("new")
    public String addBookForm(Model model, HttpSession session) {
        model.addAttribute("book", new Book());
        model.addAttribute("uid", session.getAttribute("user_id"));
        return "/books/new";
    }

    @GetMapping("{id}")
    public String viewBook(@PathVariable("id") Long id, Model model, HttpSession session) {
        model.addAttribute("book", service.find(id));
        model.addAttribute("uid", session.getAttribute("user_id"));
        return "books/view";
    }

    @PutMapping("{id}")
    public String editBook(@Valid @ModelAttribute("book") Book book, BindingResult result) {
        if(result.hasErrors()) {
            return "books/edit";
        }
        service.update(book);
        return "redirect:" + book.getId();
    }

}
