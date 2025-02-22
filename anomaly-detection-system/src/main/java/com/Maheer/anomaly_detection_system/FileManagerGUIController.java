package com.Maheer.anomaly_detection_system;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class FileManagerGUIController {

    @GetMapping("/uploader")
    public String uploader(){
        return "uploader";
    }
    }
    

