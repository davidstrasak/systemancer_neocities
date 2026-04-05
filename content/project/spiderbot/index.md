---
title: "Spiderbot"
date: 2026-03-01
tags: ["Robotics", "Hardware"]
links:
  - name: "Full Project"
    url: "https://github.com/davidstrasak/Spiderbot"
lessons:
  - "Real-world controlling"
  - "Working with li-ion batteries"
  - "See inverse kinematics in practice"
  - "Soldering on a perfboard"
---

I have always been fascinated by spider-robots so I made my own. Creating this involved making my own circuit on a perfboard, 3D printing all the parts and putting it all together with a good controlling algorithm. The spiderbot has 4 legs which have a total of 12 servos inside them.

==The circuit== starts with a 12.6V Li-Ion battery which goes into a DC/DC voltage converter to convert it to 5 Volts. These 5 Volts go into the Arduino Pro board and into the 12 MG90S servos. The arduino controls the servos using PWM through it's digital pins.

The Arduino C++ code uses the Servo.h library to control the servos (handles the PWM signal generation) and FlexiTimer2 to move smoothly between position interpolation logic.

{{< grid2 "SpiderBotWalkFront.gif" "SpiderBotWalkTop.gif" >}}
