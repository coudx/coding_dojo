package com.dojos_and_ninjas.controllers;

import com.dojos_and_ninjas.models.Ninja;
import com.dojos_and_ninjas.services.DojoService;
import com.dojos_and_ninjas.services.NinjaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.validation.Valid;

@Controller
@RequestMapping("/ninjas")
public class NinjaRoute {
    @Autowired
    private NinjaService service;
    @Autowired
    private DojoService dojoService;

    @GetMapping("/new")
    public String ninjaForm(Model model) {
        model.addAttribute("ninja", new Ninja());
        model.addAttribute("dojos", dojoService.allDojo());
        return "newNinja";
    }

    @PostMapping("/new")
    public String add(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result) {
        if(!result.hasErrors()) {
            service.add(ninja);
        }
        return "redirect:new";
    }
}
