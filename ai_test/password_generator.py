import random
import string


def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))


def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2: return "Weak"
    if score <= 3: return "Moderate"
    if score <= 4: return "Strong"
    return "Very Strong"


def main():
    while True:
        print("\n" + "=" * 50)
        print("          PASSWORD GENERATOR")
        print("=" * 50)

        while True:
            try:
                length = int(input("Password length (8-64): "))
                if 8 <= length <= 64:
                    break
                print("Please enter a length between 8 and 64.")
            except ValueError:
                print("Please enter a valid number.")

        use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() in ["yes", "y"]
        use_digits = input("Include numbers? (yes/no): ").strip().lower() in ["yes", "y"]
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() in ["yes", "y"]

        while True:
            try:
                count = int(input("How many passwords to generate? (1-10): "))
                if 1 <= count <= 10:
                    break
                print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

        print("\n" + "=" * 50)
        print("  GENERATED PASSWORDS")
        print("=" * 50)
        for i in range(count):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            strength = password_strength(pwd)
            print(f"  {i + 1}. {pwd}  [{strength}]")
        print("=" * 50)

        again = input("\nGenerate more? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
