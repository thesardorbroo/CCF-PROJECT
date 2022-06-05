package uz.hackathon.barber.dto;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.io.Serializable;

@AllArgsConstructor
@Data
public class BarbershopDto{
    private Integer id;
    private String shopName;
    private String photo;
    private String location;
    private String region;
}
