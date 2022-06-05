package uz.hackathon.barber.service;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import uz.hackathon.barber.repository.EocusRepository;

@Service
@RequiredArgsConstructor
public class EocusService{

    private final EocusRepository eocusRepository;

}
