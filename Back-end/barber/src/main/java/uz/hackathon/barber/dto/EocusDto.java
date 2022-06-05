package uz.hackathon.barber.dto;

import lombok.Data;

@Data
public class EocusDto{
    private final Integer id;
    private final Long userId;
    private final String username;
    private final String phoneNumber;
    private final String language;
    private final BarberDto barber;
    private final Integer step;
    private final String status;
}
