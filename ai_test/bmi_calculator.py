def calculate_bmi():
    print("\n" + "=" * 50)
    print("            BMI CALCULATOR")
    print("=" * 50)

    print("\nChoose unit system:")
    print("  1. Metric (kg / cm)")
    print("  2. Imperial (lbs / inches)")

    while True:
        unit = input("Your choice (1/2): ").strip()
        if unit in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    try:
        if unit == "1":
            weight = float(input("Weight (kg): "))
            height_cm = float(input("Height (cm): "))
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)
        else:
            weight = float(input("Weight (lbs): "))
            height = float(input("Height (inches): "))
            bmi = (weight / (height ** 2)) * 703

        print("\n" + "=" * 50)
        print(f"  Your BMI: {bmi:.1f}")
        print("=" * 50)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"  Category: {category}")
        print("\n  BMI Scale:")
        print("  < 18.5   Underweight")
        print("  18.5-24.9  Normal weight")
        print("  25.0-29.9  Overweight")
        print("  >= 30.0  Obese")
        print("=" * 50)

    except ValueError:
        print("Please enter valid numbers.")


def main():
    while True:
        calculate_bmi()
        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
