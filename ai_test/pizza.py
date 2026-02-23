def make_pizza():
    print("=" * 50)
    print("         PIZZA RECIPE MAKER")
    print("=" * 50)

    print("\nChoose your pizza size:")
    print("  1. Small")
    print("  2. Medium")
    print("  3. Large")

    sizes = {"1": "Small", "2": "Medium", "3": "Large"}
    while True:
        size = input("Your choice (1/2/3): ").strip()
        if size in sizes:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nChoose your base:")
    print("  1. Tomato sauce")
    print("  2. BBQ sauce")
    print("  3. Pesto")

    bases = {"1": "Tomato sauce", "2": "BBQ sauce", "3": "Pesto"}
    while True:
        base = input("Your choice (1/2/3): ").strip()
        if base in bases:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nChoose your toppings (comma separated e.g. 1,3,4):")
    print("  1. Cheese")
    print("  2. Pepperoni")
    print("  3. Mushrooms")
    print("  4. Olives")
    print("  5. Bell peppers")
    print("  6. Onions")

    toppings_map = {
        "1": "Cheese", "2": "Pepperoni", "3": "Mushrooms",
        "4": "Olives", "5": "Bell peppers", "6": "Onions"
    }

    while True:
        choices = input("Your toppings: ").strip().split(",")
        selected = [toppings_map[c.strip()] for c in choices if c.strip() in toppings_map]
        if selected:
            break
        print("Please select at least one valid topping.")

    print("\n" + "=" * 50)
    print("         YOUR PIZZA RECIPE")
    print("=" * 50)
    print(f"  Size:     {sizes[size]}")
    print(f"  Base:     {bases[base]}")
    print(f"  Toppings: {', '.join(selected)}")
    print("=" * 50)
    print("\nSteps:")
    print("  1. Preheat oven to 220°C (430°F)")
    print(f"  2. Roll out your {sizes[size].lower()} pizza dough")
    print(f"  3. Spread {bases[base].lower()} evenly over the base")
    print(f"  4. Add toppings: {', '.join(selected)}")
    print("  5. Bake for 12-15 minutes until golden and crispy")
    print("  6. Slice and enjoy!")
    print("=" * 50)


if __name__ == "__main__":
    make_pizza()
