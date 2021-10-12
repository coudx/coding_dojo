package com.language.controllers;


import com.language.models.Language;
import com.language.services.LangService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@Controller
public class MainController {
    @Autowired
    private LangService service;

    @GetMapping("/languages")
    public String index(Model model) {
        model.addAttribute("lang", new Language());
        model.addAttribute("langs", service.getAll());
        return "index";
    }

    @PostMapping("/languages")
    public String add(@Valid @ModelAttribute("lang") Language lang, BindingResult result){
        if (!result.hasErrors()) {
            service.create(lang);
        }
        return "redirect:/languages";
    }

    @GetMapping("/languages/{id}")
    public String view(@PathVariable("id") Long id, Model model){
        model.addAttribute("lang", service.find(id));
        return "view";
    }

    @GetMapping("/languages/{id}/edit")
    public String edit(@PathVariable("id") Long id, Model model) {
        model.addAttribute("lang", service.find(id));
        return "edit";
    }

    @PutMapping("/languages/{id}")
    public String update(@Valid @ModelAttribute("lang") Language lang, BindingResult result) {
        if (!result.hasErrors()) {
            service.create(lang);
        }
        return "redirect:/languages";
    }

    @DeleteMapping("/languages/{id}")
    public String del(@PathVariable("id") Long id) {
        service.delete(id);
        return "redirect:/languages";
    }

}
