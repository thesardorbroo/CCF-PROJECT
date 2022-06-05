package uz.hackathon.barber.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import uz.hackathon.barber.repository.ServiceRepository;

@Service
@RequiredArgsConstructor
public class ServiceService{
    private final ServiceRepository serviceRepository;
}
