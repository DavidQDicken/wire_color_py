low_Volt_Colors = {
  **dict.fromkeys([1, 2], "black"),
  **dict.fromkeys([3, 4], "red"),
  **dict.fromkeys([0, 5, 6], "blue")
}
high_Volt_Colors = {
  **dict.fromkeys([1, 2], "brown"),
  **dict.fromkeys([3, 4], "orange"),
  **dict.fromkeys([0, 5, 6], "yellow")
}
single_Phase_Colors = {
  **dict.fromkeys([1, 2], "black"),
  **dict.fromkeys([0, 3, 4], "red")
}

ckt_Num = int(input("Please enter a circuit number: "))

print("\nIs this a single phase or three phase circuit?")
print("NOTE: SINGLE PHASE = '1'\n      THREE PHASE = '3'\n")
phase = str(input("Please specify phase system: "))
print()

if phase == '3':
    print("\nWhat is the circuit's voltage?")
    print("NOTE: Three Phase Voltage Standards: 120, 208, 240, 277, 480\n")
    volt = str(input("Please enter a voltage: "))
    print()

    if volt == "120" or volt == "208" or volt == "240":
        print("Your wire color is " + low_Volt_Colors[ckt_Num % 6] + '.')
    elif volt == "277" or volt == "480":
        print("Your wire color is " + high_Volt_Colors[ckt_Num % 6] + '.')
    else:
        print("Invalid input")
elif phase == '1':
    print("Your wire color is " + single_Phase_Colors[ckt_Num % 4] + '.')
else:
    print("Invalid input")
