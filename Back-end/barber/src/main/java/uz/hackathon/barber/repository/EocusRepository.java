package uz.hackathon.barber.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uz.hackathon.barber.entity.Eocus;

public interface EocusRepository extends JpaRepository<Eocus, Integer> {
}