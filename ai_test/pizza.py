def make_pizza():
    print("=" * 50)
    print("         PIZZA RECIPE MAKER")
    print("=" * 50)

    print("\nChoose your pizza size:")
    print("  1. Personal (6\")")
    print("  2. Small (8\")")
    print("  3. Medium (10\")")
    print("  4. Large (12\")")
    print("  5. Extra Large (14\")")

    sizes = {"1": "Personal (6\")", "2": "Small (8\")", "3": "Medium (10\")", "4": "Large (12\")", "5": "Extra Large (14\")"}
    while True:
        size = input("Your choice (1-5): ").strip()
        if size in sizes:
            break
        print("Invalid choice. Please enter 1-5.")

    print("\nChoose your crust:")
    print("  1. Thin crust")
    print("  2. Thick crust")
    print("  3. Stuffed crust")
    print("  4. Gluten-free")

    crusts = {"1": "Thin crust", "2": "Thick crust", "3": "Stuffed crust", "4": "Gluten-free"}
    while True:
        crust = input("Your choice (1-4): ").strip()
        if crust in crusts:
            break
        print("Invalid choice. Please enter 1-4.")

    print("\nChoose your base:")
    print("  1. Tomato sauce")
    print("  2. BBQ sauce")
    print("  3. Pesto")
    print("  4. Garlic butter")
    print("  5. Cream sauce")

    bases = {"1": "Tomato sauce", "2": "BBQ sauce", "3": "Pesto", "4": "Garlic butter", "5": "Cream sauce"}
    while True:
        base = input("Your choice (1-5): ").strip()
        if base in bases:
            break
        print("Invalid choice. Please enter 1-5.")

    print("\nChoose your cheese:")
    print("  1. Mozzarella")
    print("  2. Cheddar")
    print("  3. Parmesan")
    print("  4. Vegan cheese")
    print("  5. Four cheese blend")

    cheeses = {"1": "Mozzarella", "2": "Cheddar", "3": "Parmesan", "4": "Vegan cheese", "5": "Four cheese blend"}
    while True:
        cheese = input("Your choice (1-5): ").strip()
        if cheese in cheeses:
            break
        print("Invalid choice. Please enter 1-5.")

    print("\nChoose your toppings (comma separated e.g. 1,3,4):")
    print("  1.  Pepperoni")
    print("  2.  Mushrooms")
    print("  3.  Olives")
    print("  4.  Bell peppers")
    print("  5.  Onions")
    print("  6.  Chicken")
    print("  7.  Bacon")
    print("  8.  Pineapple")
    print("  9.  Spinach")
    print("  10. Sun-dried tomatoes")
    print("  11. Jalapeños")
    print("  12. Anchovies")

    toppings_map = {
        "1": "Pepperoni", "2": "Mushrooms", "3": "Olives",
        "4": "Bell peppers", "5": "Onions", "6": "Chicken",
        "7": "Bacon", "8": "Pineapple", "9": "Spinach",
        "10": "Sun-dried tomatoes", "11": "Jalapeños", "12": "Anchovies"
    }

    while True:
        choices = input("Your toppings: ").strip().split(",")
        selected = [toppings_map[c.strip()] for c in choices if c.strip() in toppings_map]
        if selected:
            break
        print("Please select at least one valid topping.")

    print("\nChoose your finishing drizzle (optional):")
    print("  1. Olive oil")
    print("  2. Chilli oil")
    print("  3. Honey")
    print("  4. Balsamic glaze")
    print("  5. None")

    drizzles = {"1": "Olive oil", "2": "Chilli oil", "3": "Honey", "4": "Balsamic glaze", "5": "None"}
    while True:
        drizzle = input("Your choice (1-5): ").strip()
        if drizzle in drizzles:
            break
        print("Invalid choice. Please enter 1-5.")

    print("\n" + "=" * 50)
    print("         YOUR PIZZA RECIPE")
    print("=" * 50)
    print(f"  Size:     {sizes[size]}")
    print(f"  Crust:    {crusts[crust]}")
    print(f"  Base:     {bases[base]}")
    print(f"  Cheese:   {cheeses[cheese]}")
    print(f"  Toppings: {', '.join(selected)}")
    if drizzles[drizzle] != "None":
        print(f"  Drizzle:  {drizzles[drizzle]}")
    print("=" * 50)
    print("\nSteps:")
    print("  1. Preheat oven to 220°C (430°F)")
    print(f"  2. Roll out your {crusts[crust].lower()} dough to {sizes[size].lower()}")
    print(f"  3. Spread {bases[base].lower()} evenly over the base")
    print(f"  4. Add {cheeses[cheese].lower()}")
    print(f"  5. Add toppings: {', '.join(selected)}")
    if drizzles[drizzle] != "None":
        print(f"  6. Drizzle with {drizzles[drizzle].lower()}")
        print("  7. Bake for 12-15 minutes until golden and crispy")
        print("  8. Slice and enjoy!")
    else:
        print("  6. Bake for 12-15 minutes until golden and crispy")
        print("  7. Slice and enjoy!")
    print("=" * 50)


if __name__ == "__main__":
    make_pizza()
