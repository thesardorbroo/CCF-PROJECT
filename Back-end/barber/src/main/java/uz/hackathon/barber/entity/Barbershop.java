package uz.hackathon.barber.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "barbershop")
public class Barbershop {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Integer id;

    @Column(name = "shop_name", length = 64)
    private String shopName;

    @Column(name = "photo")
    private String photo;

    @Column(name = "location", length = 64)
    private String location;

    @Column(name = "region")
    private String region;

}