import serial

# 30 = 1E
# 60 = 3C
# 70 = 46
# 75 = 4B
# 80 = 50
# 85 = 55
# 90 = 5A
# 100 = 64
# 120 = 78
# 150 = 96
# 180 = B4
# 200 = C8
# 1000 = 3E8
# 2000 = 7D0
# 2500 = 9C4
# 3000 = BB8
# 4000 = FA0
# 5000 = 1388

packet=[]
packet.append(b'\x16') # SYNC
packet.append(b'\x05') # select = uint8
packet.append(b'\x3C') # LRL = uint8 60 = 3C, 120 = 78
packet+= [b'\xC8\x00'] # Refrac Period = uint16     
packet+= [b'\x96\x00'] # AV Delay = uint16
packet.append(b'\x01') # APW = uint8
packet.append(b'\x01') # VPW = uint8
packet+= [b'\xB4\x0B'] # Amplitude = uint16
packet.append(b'\x50') # Sensing Threshold = uint8
packet.append(b'\x03') # Activity Threshold = uint8
packet.append(b'\x08') # RF = uint8
packet.append(b'\x01') # rate_adapt = uint8
packet.append(b'\xB4') # MSR = uint8
packet.append(b'\x01') # Recovery time = uint8
packet.append(b'\x10') # Reaction time = uint8

packet.append('close') # end of message

ser = serial.Serial()

# Change to your COM Port for the pacemaker
ser.port = 'COM11' 
ser.buadrate=9600
ser.open()

for pack in packet:
    if pack == 'close':
        break

    ser.write(pack)
    print(pack)
ser.close()

