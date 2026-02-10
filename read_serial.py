import matplotlib.pyplot as plt
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
        plt.figure(figsize=(10, 6))
        plt.plot(temps, 'b-', linewidth=2)
        plt.axhline(y=avg, color='green', linestyle='--',
                    label=f'Average: {avg:.2f}°C')
        plt.axhline(y=22, color='r', linestyle='--', label='Max Threshold')
        plt.axhline(y=18, color='cyan', linestyle='--', label='Min Threshold')
        plt.xlabel('Reading Number')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Data from Arduino')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No valid data collected")
