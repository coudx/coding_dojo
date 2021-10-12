package com.language.repos;

import com.language.models.Language;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LangRepo extends CrudRepository<Language, Long> {
    List<Language> findAll();
}
