package com.counter.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;

@Controller
public class MainController {
    @RequestMapping("/")
    public String index(HttpSession session){
        if (session.getAttribute("n") == null) {
            session.setAttribute("n", 1);
        } else {
            session.setAttribute("n", (Integer) session.getAttribute("n") + 1);
        }
        return "index";
    }

    @RequestMapping("/counter")
    public String counter(HttpSession session) {
        if (session.getAttribute("n") == null) {
            session.setAttribute("n", 0);
        }
        return "counter";
    }
}
