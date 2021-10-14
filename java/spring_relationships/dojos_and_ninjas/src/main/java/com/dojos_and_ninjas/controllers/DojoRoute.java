package com.dojos_and_ninjas.controllers;

import com.dojos_and_ninjas.models.Dojo;
import com.dojos_and_ninjas.services.DojoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@Controller
@RequestMapping("/dojos")
public class DojoRoute {
    @Autowired
    private DojoService service;

    @GetMapping("/new")
    public String dojoForm(Model model) {
        model.addAttribute("dojo", new Dojo());
        return "newDojo";
    }

    @PostMapping("/new")
    public String add(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
        if(!result.hasErrors()){
            service.add(dojo);
        }
        return "redirect:new";
    }

    @GetMapping("/{x}")
    public String dojo(@PathVariable("x") Long x, Model model) {
        model.addAttribute("dojo", service.find(x));
        return "dojoView";
    }
}
