package com.dojos_and_ninjas.services;

import com.dojos_and_ninjas.models.Ninja;
import com.dojos_and_ninjas.repos.NinjaRepo;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NinjaService {
    private final NinjaRepo repo;

    public NinjaService(NinjaRepo repo) { this.repo = repo; }

    public List<Ninja> allNinja() { return repo.findAll(); }

    public Ninja add(Ninja x) { return repo.save(x); }
}
