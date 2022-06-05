package uz.hackathon.barber.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uz.hackathon.barber.entity.Service;

public interface ServiceRepository extends JpaRepository<Service, Integer> {
}