package com.dojos_and_ninjas.repos;

import com.dojos_and_ninjas.models.Dojo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DojoRepo extends CrudRepository<Dojo, Long> {
    List<Dojo> findAll();
}
