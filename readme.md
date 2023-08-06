# BrickPiRover

This program serves as the main logic / controller for a BrickPi based rover.  This allows for remote input using Udp protocol (through a companion project called BrickPiRemote).


## Instructions

Install Python 3.7.3 & pip: 

    sudo apt-get install python3-pip

Setup git:

    sudo apt update
    sudo apt install git

Clone the Rover code:

    git clone git@github.com:kevinbyrom/BrickPiRover.git

Install BrickPi module [instructions](https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/):

    curl -kL dexterindustries.com/update_brickpi3 | bash
    sudo reboot

Configure settings

Run the Rover: 

    cd ~
    python3 BrickPiRover/main.py
