package uz.hackathon.barber.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uz.hackathon.barber.entity.Order;

public interface OrderRepository extends JpaRepository<Order, Integer> {
}