import matplotlib.pyplot as plt
import numpy as np

fileObj = open('sem3/1kHz_44100Hz_16bit_05sec.wav', mode='rb')

data=fileObj.read()

file_size_inbytes = data[4:8] 
file_size = int.from_bytes(file_size_inbytes, byteorder = "little")

chan_num_inbyte = data[22:24]
chan_num = int.from_bytes(chan_num_inbyte, byteorder = "little")

aud_data_size_inbytes = data[40:44]
aud_data_size = int.from_bytes(aud_data_size_inbytes, byteorder = "little")

sample_rate_inbytes = data [24:28]
sample_rate = int.from_bytes(sample_rate_inbytes, byteorder = "little")

aud_amps = []

for i in range (0, aud_data_size,2):
    amp_inbytes = data[44+i:i+2+44]
    amp = int.from_bytes(amp_inbytes, byteorder = "little", signed = True)
    aud_amps.append(amp)

time = np.linspace(0,len(aud_amps)/sample_rate,len(aud_amps))

plt.plot(time,aud_amps)
plt.show()

#print(file_size_inbytes)
#print(file_size)
#print(chan_num)
#print(aud_data_size)
#print(sample_rate)
#print(aud_amps)
