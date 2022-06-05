package uz.hackathon.barber.mapping;

import uz.hackathon.barber.dto.BarberDto;
import uz.hackathon.barber.entity.Barber;

import java.util.List;
import java.util.stream.Collectors;

public class BarberMapping {

    public static BarberDto toDto(Barber barber){
        return barber == null ? null
                :new BarberDto(
                        barber.getId(), barber.getUserId(),
                barber.getPhoto(), barber.getFullName(),
                null, barber.getStartTime(),
                barber.getEndTime(), barber.getKey()
        );
    }

    public static List<BarberDto> toDtos(List<Barber> barbers){
        return barbers.stream().map(a -> toDto(a)).collect(Collectors.toList());
    }
}
