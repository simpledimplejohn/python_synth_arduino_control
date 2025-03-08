# Python Synth with Arduino Control

## About
A python based modular sythisizer MVP, designed to run on my personal macbook
but have an Arduino controler that I build using pots, buttons, sensors.

## Setup
### 1. Create a Virtual Environment
```bash
python3 -m venv synth_venv
source synth_venv/bin/activate  # Activate venv
pip install pyserial numpy sounddevice pyqtgraph
pip install PyQt6


```
### 2. Arduion


## Run
1. Run Arduino
- Connect USB
- Find its port 
````bash
ls /dev/tty.usbmodem*
````
- update the synth.py script with the port 

2. Run Python 
````bash
source synth_venv/bin/activate
python3 ./synth.py
```

