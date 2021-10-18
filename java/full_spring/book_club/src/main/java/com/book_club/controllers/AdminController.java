package com.book_club.controllers;

import com.book_club.models.LoginUser;
import com.book_club.models.User;
import com.book_club.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

@Controller
@RequestMapping
public class AdminController {

    @Autowired
    private UserService service;

    @GetMapping
    public String index(Model model) {
        model.addAttribute("reg", new User());
        model.addAttribute("login", new LoginUser());
        return "index";
    }

    @PostMapping("login")
    public String login(@Valid @ModelAttribute("login") LoginUser login, BindingResult result, HttpSession session) {
        User user = service.login(login, result);
        if(!result.hasErrors()) {
            session.setAttribute("user_id", user.getId());
            return "redirect:/books";
        }
        return "redirect:";
    }

    @PostMapping("register")
    public String reg(@Valid @ModelAttribute("reg") User reg, BindingResult result, HttpSession session) {
        service.register(reg, result);
        if(!result.hasErrors()) {
            session.setAttribute("user_id", reg.getId());
            return "redirect:/books";
        }
        return "redirect:";
    }
}
