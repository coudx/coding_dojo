package com.pokebook.controllers;

import com.pokebook.models.Pokebook;
import com.pokebook.services.PokebookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@Controller
public class PokeBookRoute {

    @Autowired
    private PokebookService service;

    @GetMapping("/expense")
    public String index(Model model){
        model.addAttribute("pokebooks", service.allBooks());
        model.addAttribute("poke", new Pokebook());
        return "index";
    }

    @PostMapping("/expense/add")
    public String add(@Valid @ModelAttribute("poke") Pokebook newPokebook, BindingResult result){
        if (!result.hasErrors()) {
            service.createBook(newPokebook);
        }
        return "redirect:/expense";
    }

    @GetMapping("/expense/edit/{id}")
    public String edit(@PathVariable("id") Long id, Model model) {
        model.addAttribute("poke", service.findBook(id));
        return "edit";
    }

    @PutMapping("/expense/edit/{id}")
    public String update(@Valid @ModelAttribute("poke") Pokebook poke, BindingResult result){
        if (!result.hasErrors()){
            service.updateBook(poke);
        }
        return "redirect:/expense";
    }

}
