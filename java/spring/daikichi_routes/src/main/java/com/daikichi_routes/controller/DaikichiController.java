package com.daikichi_routes.controller;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DaikichiController {
    @RequestMapping("/daikichi")
    public String daikichi() {
        return "Welcome!";
    }

    @RequestMapping("/daikichi/{day}")
    public String today(@PathVariable("day") String day){
        if(day.contains("today")) {
            return "Today you will find luck in all your endeavors!";
        } else if (day.contains("tomorrow")) {
            return "Tomorrow, an opportunity will arise, so be sure to open to new ideas!";
        }
        return "Oops!";
    }
}
