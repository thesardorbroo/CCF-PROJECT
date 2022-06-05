package uz.hackathon.barber.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import uz.hackathon.barber.dto.BarberDto;
import uz.hackathon.barber.dto.ResponseDTO;
import uz.hackathon.barber.service.BarberService;

import java.util.List;

@RestController
@RequestMapping("/barber")
@RequiredArgsConstructor
public class BarberController {
    private final BarberService barberService;

    @GetMapping("get-all")
    public ResponseDTO<List<BarberDto>> getAll(){
        return barberService.getAll();
    }
}
