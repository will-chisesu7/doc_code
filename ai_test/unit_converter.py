def convert_length():
    print("\n  Length Conversions:")
    print("  1. Kilometres to Miles")
    print("  2. Miles to Kilometres")
    print("  3. Metres to Feet")
    print("  4. Feet to Metres")

    choice = input("  Your choice (1-4): ").strip()
    try:
        value = float(input("  Enter value: "))
        if choice == "1":
            print(f"  {value} km = {value * 0.621371:.4f} miles")
        elif choice == "2":
            print(f"  {value} miles = {value * 1.60934:.4f} km")
        elif choice == "3":
            print(f"  {value} m = {value * 3.28084:.4f} feet")
        elif choice == "4":
            print(f"  {value} feet = {value * 0.3048:.4f} m")
        else:
            print("  Invalid choice.")
    except ValueError:
        print("  Please enter a valid number.")


def convert_weight():
    print("\n  Weight Conversions:")
    print("  1. Kilograms to Pounds")
    print("  2. Pounds to Kilograms")
    print("  3. Grams to Ounces")
    print("  4. Ounces to Grams")

    choice = input("  Your choice (1-4): ").strip()
    try:
        value = float(input("  Enter value: "))
        if choice == "1":
            print(f"  {value} kg = {value * 2.20462:.4f} lbs")
        elif choice == "2":
            print(f"  {value} lbs = {value * 0.453592:.4f} kg")
        elif choice == "3":
            print(f"  {value} g = {value * 0.035274:.4f} oz")
        elif choice == "4":
            print(f"  {value} oz = {value * 28.3495:.4f} g")
        else:
            print("  Invalid choice.")
    except ValueError:
        print("  Please enter a valid number.")


def convert_temperature():
    print("\n  Temperature Conversions:")
    print("  1. Celsius to Fahrenheit")
    print("  2. Fahrenheit to Celsius")
    print("  3. Celsius to Kelvin")
    print("  4. Kelvin to Celsius")

    choice = input("  Your choice (1-4): ").strip()
    try:
        value = float(input("  Enter value: "))
        if choice == "1":
            print(f"  {value}°C = {(value * 9/5) + 32:.2f}°F")
        elif choice == "2":
            print(f"  {value}°F = {(value - 32) * 5/9:.2f}°C")
        elif choice == "3":
            print(f"  {value}°C = {value + 273.15:.2f}K")
        elif choice == "4":
            print(f"  {value}K = {value - 273.15:.2f}°C")
        else:
            print("  Invalid choice.")
    except ValueError:
        print("  Please enter a valid number.")


def convert_speed():
    print("\n  Speed Conversions:")
    print("  1. km/h to mph")
    print("  2. mph to km/h")
    print("  3. m/s to km/h")
    print("  4. km/h to m/s")

    choice = input("  Your choice (1-4): ").strip()
    try:
        value = float(input("  Enter value: "))
        if choice == "1":
            print(f"  {value} km/h = {value * 0.621371:.4f} mph")
        elif choice == "2":
            print(f"  {value} mph = {value * 1.60934:.4f} km/h")
        elif choice == "3":
            print(f"  {value} m/s = {value * 3.6:.4f} km/h")
        elif choice == "4":
            print(f"  {value} km/h = {value / 3.6:.4f} m/s")
        else:
            print("  Invalid choice.")
    except ValueError:
        print("  Please enter a valid number.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("            UNIT CONVERTER")
        print("=" * 50)
        print("  1. Length")
        print("  2. Weight")
        print("  3. Temperature")
        print("  4. Speed")
        print("  5. Exit")
        print("=" * 50)

        choice = input("\nChoose a category (1-5): ").strip()

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            convert_speed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
