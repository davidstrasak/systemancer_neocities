---
title: "Conveyor Controller"
date: 2025-07-05
tags: ["Hardware", "Controller"]
links:
  - name: "Arduino Code"
    url: "https://github.com/davidstrasak/Bachelors_code"
  - name: "Phone app Code"
    url: "https://github.com/davidstrasak/Bachelors_PhoneApp"
  - name: "PCB Design files"
    url: "https://github.com/davidstrasak/Bachelors_PCB"
lessons:
  - "Found my passion for electronics and PCB design"
  - "Creating mobile applications"
  - "Got way better at soldering"
  - "Learned to host a ESP8266 WebServer and control the microcontroller through it"
  - "Learned the importance of state diagrams"
---

This project is my Bachelor's thesis where I was tasked with designing an intuitive device which controls the movement of conveyors through a mobile app, so mechanical engineers have an easier time when commissioning conveyor installation quality (specifically when they are looking if the conveyor runs smoothly).

I made my own PCB, added in a ==WEMOS D1 Mini development board== with an ==ESP8266 microcontroller== unit, wired everything with relays so I am able to switch the control panel inputs to the frequency drive and I created the app through which it can all be controlled thanks to a shared WiFi hotspot that all the devices are connected to.

A cool thing about this project is that ==the mobile app not only enables me to control the conveyor==, but it can have all the instructions for setup and troubleshooting the device and parts of the system. And since it's on mobile you do not need any additional devices :D.

This was a really interesting challenge with lots of different systems that intertwine into each other and it was ==my hardest challenge where I was solving the most issues :D.==

![A box with some buttons and a display on it, which is used to control the conveyor](ConveyorController_Physical.png)
