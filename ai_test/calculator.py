import math


def calculate():
    print("=" * 50)
    print("             CALCULATOR")
    print("=" * 50)
    print("  Basic:      +  -  *  /  // % **")
    print("  Scientific: sqrt  sin  cos  tan  log  log10")
    print("=" * 50)

    while True:
        expression = input("\nEnter calculation (or 'quit' to exit): ").strip().lower()

        if expression == "quit":
            break

        try:
            expression = expression.replace("sqrt(", "math.sqrt(")
            expression = expression.replace("sin(", "math.sin(math.radians(")
            expression = expression.replace("cos(", "math.cos(math.radians(")
            expression = expression.replace("tan(", "math.tan(math.radians(")
            expression = expression.replace("log10(", "math.log10(")
            expression = expression.replace("log(", "math.log(")

            # Close extra parentheses for trig functions
            for func in ["sin", "cos", "tan"]:
                if f"math.{func}" in expression:
                    expression = expression + ")"

            result = eval(expression, {"__builtins__": {}}, {"math": math})
            print(f"  Result: {result}")
        except Exception:
            print("  Invalid expression. Please try again.")


if __name__ == "__main__":
    calculate()
