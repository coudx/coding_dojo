package com.language.services;

import com.language.models.Language;
import com.language.repos.LangRepo;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LangService {
    private final LangRepo repo;

    public LangService(LangRepo repo){
        this.repo = repo;
    }

    public List<Language> getAll() { return repo.findAll(); }

    public Language create(Language a) {return repo.save(a); }

    public Language find(Long id) { return repo.findById(id).orElse(null);}

    public Language update(Language a) {return repo.save(a); }

    public void delete(Long id) { repo.deleteById(id);}
}
