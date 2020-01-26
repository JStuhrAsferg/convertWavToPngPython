import time
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

start_time = time.time()

spf = wave.open("pcm1608s.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, "int16")

outputFilename = str(time.time())
outputFilename = outputFilename + '.png'
plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
#plt.show()
plt.savefig(outputFilename, orientation='portrait', facecolor='w')

print("--- %s seconds ---" % (time.time() - start_time))