# Instructions

1. Install Python 3.7.3 & pip 

    sudo apt-get install python3-pip

2. Setup git

    sudo apt update
    sudo apt install git

3. Clone the Rover code

    git clone git@github.com:kevinbyrom/BrickPiRover.git

4. Install BrickPi module [instructions](https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/)

    curl -kL dexterindustries.com/update_brickpi3 | bash
    sudo reboot

4. Configure settings
5. Run the Rover 

    cd ~
    python3 BrickPiRover/main.py
