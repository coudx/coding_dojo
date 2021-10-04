package com.display_date.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import java.text.SimpleDateFormat;
import java.util.Date;

@Controller
public class Route {
    @RequestMapping("/")
    public String index(){
        return "index";
    }

    @RequestMapping("/date")
    public String date(Model x){
        Date now = new Date();
        SimpleDateFormat ft = new SimpleDateFormat("E', the' dd 'of' MMM', 'y");
        x.addAttribute("date", ft.format(now));
        return "date";
    }

    @RequestMapping("/time")
    public String time(Model x){
        Date now = new Date();
        SimpleDateFormat ft = new SimpleDateFormat("hh:mm a");
        x.addAttribute("time", ft.format(now));
        return "time";
    }
}
