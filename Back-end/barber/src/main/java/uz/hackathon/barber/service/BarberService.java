package uz.hackathon.barber.service;


import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import uz.hackathon.barber.dto.BarberDto;
import uz.hackathon.barber.dto.BarbershopDto;
import uz.hackathon.barber.dto.ResponseDTO;
import uz.hackathon.barber.entity.Barber;
import uz.hackathon.barber.entity.Barbershop;
import uz.hackathon.barber.mapping.BarberMapping;
import uz.hackathon.barber.mapping.BarbershopMapping;
import uz.hackathon.barber.repository.BarberRepository;
import uz.hackathon.barber.repository.BarbershopRepository;

import java.util.List;
import java.util.stream.Collectors;

import static uz.hackathon.barber.mapping.BarberMapping.toDtos;

@Service
@RequiredArgsConstructor
public class BarberService{
    private final BarberRepository barberRepository;
    private final BarbershopRepository barbershopRepository;


    public ResponseDTO<List<BarberDto>> getAll(){
        try {
           List<Barber> barbers = barberRepository.findAll();
            return new ResponseDTO<>(true, barbers.stream().map(b -> {
                BarbershopDto barbershop = (BarbershopMapping.toDto(barbershopRepository.findById(b.getBarbershopId()).get()));
                BarberDto barberDto = BarberMapping.toDto(b);
                barberDto.setBarbershopDto(barbershop);
                return barberDto;
            }).collect(Collectors.toList()));
        }catch(Exception e){
            e.printStackTrace();
            return new ResponseDTO<>(false, null);
        }
    }
}
