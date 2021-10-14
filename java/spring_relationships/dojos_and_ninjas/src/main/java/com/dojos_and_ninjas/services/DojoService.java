package com.dojos_and_ninjas.services;

import com.dojos_and_ninjas.models.Dojo;
import com.dojos_and_ninjas.repos.DojoRepo;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DojoService {
    private final DojoRepo repo;

    public DojoService(DojoRepo repo) { this.repo = repo; }

    public List<Dojo> allDojo() { return repo.findAll(); }

    public Dojo add(Dojo x) { return repo.save(x); }

    public Dojo find(Long id) { return repo.findById(id).orElse(null); }
}
