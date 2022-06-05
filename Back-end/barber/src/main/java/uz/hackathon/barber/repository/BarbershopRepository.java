package uz.hackathon.barber.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uz.hackathon.barber.entity.Barbershop;

public interface BarbershopRepository extends JpaRepository<Barbershop, Integer> {
}