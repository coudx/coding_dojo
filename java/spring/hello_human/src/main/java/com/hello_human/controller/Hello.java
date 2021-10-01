package com.hello_human.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Hello {
    @RequestMapping("/")
    public String index(@RequestParam(required = false) String name, @RequestParam(required = false) String lastname) {
        String line = "Hello ";
        if (name != null){
            line += name + " ";
        }
        if (lastname != null) {
            line += lastname;
        }
        return line;
    }
}
