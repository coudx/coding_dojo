package com.pokebook.controllers;

import com.pokebook.models.Pokebook;
import com.pokebook.services.PokebookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import javax.validation.Valid;

@Controller
public class PokeBookRoute {

    @Autowired
    private PokebookService service;

    @GetMapping("/expense")
    public String index(Model model){
        model.addAttribute("pokebooks", service.allBooks());
        model.addAttribute("newPoke", new Pokebook());
        return "index";
    }

    @PostMapping("/expense/add")
    public String add(@Valid @ModelAttribute("newPoke") Pokebook newPokebook, BindingResult result){
        if (!result.hasErrors()) {
            service.createBook(newPokebook);
        }
        return "redirect:/expense";
    }

}
