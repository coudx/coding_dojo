package com.omikuji_form.controller;

import org.springframework.stereotype.Controller;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.servlet.http.HttpSession;
import java.util.ArrayList;
import java.util.Map;

import static org.springframework.web.bind.annotation.RequestMethod.*;

@Controller
public class Route {
    @RequestMapping("/omikuji")
    public String index(){
        return "omikuji";
    }

    @RequestMapping(value="/omikuji", method=RequestMethod.POST)
    public String submit(
            @RequestParam(value="year") String year,
            @RequestParam(value="city") String city,
            @RequestParam(value="name") String name,
            @RequestParam(value="hobby") String hobby,
            @RequestParam(value="type") String type,
            @RequestParam(value="etc") String etc,
            HttpSession session, RedirectAttributes rA){
        int n = Integer.parseInt(year);
        if (n > 4 && n < 26){
            session.setAttribute("year", year);
            session.setAttribute("city", city);
            session.setAttribute("name", name);
            session.setAttribute("hobby", hobby);
            session.setAttribute("type", type);
            session.setAttribute("etc", etc);
            return "redirect:/omikuji/show";
        } else {
            rA.addFlashAttribute("error", "Value need to be within requirements");
            return "redirect:/omikuji";
        }

    }

    @RequestMapping("/omikuji/show")
    public String show(){
        return "show";
    }
}
