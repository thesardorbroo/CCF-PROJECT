package uz.hackathon.barber.dto;


import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalTime;
@AllArgsConstructor
@Data
public class BarberDto{
    private Integer id;
    private Long userId;
    private String photo;
    private String fullName;
    private BarbershopDto barbershopDto;
    private String workTime;
    private String key;

    public BarberDto(Integer id, Long userId, String photo, String fullName, BarbershopDto barbershopDto, LocalTime startTime, LocalTime endTime, String key) {
        this.id = id;
        this.userId = userId;
        this.photo = photo;
        this.fullName = fullName;
        this.barbershopDto = barbershopDto;
        this.workTime = startTime + " - " + endTime;
        this.key = key;
    }

}
