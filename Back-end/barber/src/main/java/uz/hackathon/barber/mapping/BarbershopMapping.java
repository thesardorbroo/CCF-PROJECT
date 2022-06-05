package uz.hackathon.barber.mapping;

import uz.hackathon.barber.dto.BarbershopDto;
import uz.hackathon.barber.entity.Barbershop;

public class BarbershopMapping {

    public static BarbershopDto toDto(Barbershop barbershop){
        return barbershop == null ? null
                :new BarbershopDto(barbershop.getId(),
                barbershop.getShopName(), barbershop.getPhoto(),
                barbershop.getLocation(), barbershop.getRegion());
    }
}
