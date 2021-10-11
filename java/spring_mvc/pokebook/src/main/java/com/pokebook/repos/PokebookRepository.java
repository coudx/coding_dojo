package com.pokebook.repos;

import com.pokebook.models.Pokebook;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PokebookRepository extends CrudRepository<Pokebook, Long> {
    List<Pokebook> findAll();
}
