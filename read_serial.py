import serial
import time

ser = serial.Serial(port='COM5', baudrate=9600)
temps = []
print(f"\n To exit -- Ctrl + C")
try:
    while True:
        value = ser.readline()
        valueInString = str(value, 'UTF-8')
        print(valueInString)

        try:
            temp = float(valueInString)
            temps.append(temp)
        except ValueError:
            pass
except KeyboardInterrupt:
    time.sleep(1)
    print("\n\nData collection stopped")

finally:
    ser.close()
    if len(temps) > 0:
        avg = sum(temps) / len(temps)
        print(f"\n --Statistics--")
        time.sleep(2)
        print(f"\n Average Temperature: {avg:.2f}°C")
        print(f"Max Temperature: {max(temps):.2f}°C")
        print(f"Min Temperature: {min(temps):.2f}°C")

    else:
        print("No valid data collected")
