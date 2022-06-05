package uz.hackathon.barber.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uz.hackathon.barber.entity.Barber;

public interface BarberRepository extends JpaRepository<Barber, Integer> {
}