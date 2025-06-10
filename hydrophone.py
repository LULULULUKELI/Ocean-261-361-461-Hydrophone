from machine import Pin, ADC
from time import sleep

adc = ADC(0)

# ✅ Manually set your column name here
column_name = "trial5"  # 👈 change this each time you run the code

# Open or create a CSV file on the microcontroller's filesystem
datafile = open("location3_may28.csv", "a")  # appends to the same file

# Write a header for this batch of data
datafile.write(f"\nreading_number,{column_name}\n")

for i in range(20):  # take 10 readings
    voltage_fraction_1 = adc.read() / 1024
    voltage_fraction_2 = adc.read() / 1024

    # Print to serial
    print(f"{i*2+1}: {voltage_fraction_1}")
    print(f"{i*2+2}: {voltage_fraction_2}")

    # Write both readings to the CSV with an index
    datafile.write(f"{i*2+1},{voltage_fraction_1}\n")
    datafile.write(f"{i*2+2},{voltage_fraction_2}\n")

    sleep(1)

datafile.close()
