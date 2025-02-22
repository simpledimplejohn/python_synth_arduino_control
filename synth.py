import serial
import numpy as np
import sounddevice as sd
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
import sys

# Update with the correct Arduino port
arduino_port = "/dev/tty.usbmodem*"  
ser = serial.Serial(arduino_port, 9600)

SAMPLE_RATE = 44100
BUFFER_SIZE = 1024

# PyQtGraph Setup
app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(title="Real-Time Audio Waveform")
plot = win.addPlot(title="Waveform")
curve = plot.plot()
plot.setYRange(-1, 1)

waveform = np.zeros(BUFFER_SIZE)

def get_arduino_data():
    """ Read potentiometer values from Arduino. """
    try:
        line = ser.readline().decode('utf-8').strip()
        freq_val, amp_val = map(int, line.split(","))
        frequency = np.interp(freq_val, [0, 1023], [100, 2000])
        amplitude = np.interp(amp_val, [0, 1023], [0.0, 1.0])
        return frequency, amplitude
    except:
        return 440, 0.5  

def audio_callback(outdata, frames, time, status):
    """ Generate a sine wave based on potentiometer values. """
    global waveform
    frequency, amplitude = get_arduino_data()
    t = (np.arange(frames) + audio_callback.phase) / SAMPLE_RATE
    waveform = amplitude * np.sin(2 * np.pi * frequency * t)
    outdata[:] = waveform.reshape(-1, 1)
    audio_callback.phase += frames

audio_callback.phase = 0

# Start Audio Stream
stream = sd.OutputStream(channels=1, samplerate=SAMPLE_RATE, callback=audio_callback)
stream.start()

# Update Plot in Real-Time
def update_plot():
    curve.setData(waveform)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update_plot)
timer.start(50)

print("Playing... Close the window to stop.")
win.show()
sys.exit(app.exec_())
