import serial
import time

if __name__ == '__main__':
    
    # Setup serial communication 
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        # Send text over serial, the Arduino will look for this keyword and do an action in response
        ser.write(b"On\n")
        time.sleep(1)
        ser.write(b"Off\n")
        
        # If there is a serial message waiting
        if ser.in_waiting > 0:
            
            # Decode and write it out to console
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
