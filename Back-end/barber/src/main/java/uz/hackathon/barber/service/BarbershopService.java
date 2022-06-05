package uz.hackathon.barber.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import uz.hackathon.barber.repository.BarbershopRepository;


@Service
@RequiredArgsConstructor
public class BarbershopService {
    private final BarbershopRepository bShopRepository;



}
