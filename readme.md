# Instructions

1. Install Python 3.7.3 & pip 

    sudo apt-get install python3-pip

2. Setup git

    sudo apt update
    sudo apt install git

3. Clone the Rover code

    git clone git@github.com:kevinbyrom/BrickPiRover.git

4. Install BrickPi module [instructions](https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/program-it/python/#:~:text=Installation,directory)

    git clone git@github.com:kevinbyrom/BrickPi3.git
    cd BrickPi3/Software/Python
    sudo apt-get install python-setuptools
    sudo python setup.py install

4. Configure settings
5. Run the Rover 

    cd ~
    python3 BrickPiRover/main.py
