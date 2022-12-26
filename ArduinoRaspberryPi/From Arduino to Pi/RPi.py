import serial

if __name__ == '__main__':
    
    # Set up our serial communication, you will need to change ttyUSB0 to match your serial port, 9600 is the baud rate
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        # If there is a serial message waiting
        if ser.in_waiting > 0:
            # Decode it and print it to the console
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
