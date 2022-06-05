package uz.hackathon.barber.dto;

import lombok.Data;

import java.time.LocalDate;
import java.time.LocalTime;

@Data
public class OrderDto{
    private final Integer id;
    private final BarberDto barber;
    private final EocusDto customer;
    private final LocalTime orderTime;
    private final LocalDate orderDay;
}
