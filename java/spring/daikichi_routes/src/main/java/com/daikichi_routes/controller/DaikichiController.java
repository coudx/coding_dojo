package com.daikichi_routes.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class DaikichiController {
    @GetMapping("")
    public String daikichi() {
        return "Welcome!";
    }

    @GetMapping("/{day}")
    public String today(@PathVariable("day") String day){
        if(day.contains("today")) {
            return "Today you will find luck in all your endeavors!";
        } else if (day.contains("tomorrow")) {
            return "Tomorrow, an opportunity will arise, so be sure to open to new ideas!";
        }
        return "Oops!";
    }

    @GetMapping("/travel/{place}")
    public String travel(@PathVariable("place") String place){
        return "Congratulations! You will soon travel to " + place;
    }

    @GetMapping("/lotto/{n}")
    public String lotto(@PathVariable("n") Integer n){
        if ( n%2 == 1 ){
            return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
        } else {
            return "You will take a grand journey in the near future, but be weary of tempting offers.";
        }
    }
}
