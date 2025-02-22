# Python Synth with Arduino Control

## About
A python based modular sythisizer MVP, designed to run on my personal macbook
but have an Arduino controler that I build using pots, buttons, sensors.

## Setup
### 1. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Activate venv
pip install pyserial numpy sounddevice pyqtgraph
```

## Run
````bash
source venv/bin/activate
python3 ./py_synth.py
```