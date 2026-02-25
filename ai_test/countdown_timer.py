import time


def countdown(seconds):
    print("\n" + "=" * 50)
    print("  Timer started! Press Ctrl+C to cancel.")
    print("=" * 50)

    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            print(f"\r  Time remaining: {hours:02d}:{mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            seconds -= 1

        print("\r  Time remaining: 00:00:00")
        print("\n" + "=" * 50)
        print("  *** TIME IS UP! ***")
        print("=" * 50)

    except KeyboardInterrupt:
        print("\n\nTimer cancelled.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("           COUNTDOWN TIMER")
        print("=" * 50)

        try:
            hours = int(input("Hours: ") or 0)
            minutes = int(input("Minutes: ") or 0)
            seconds = int(input("Seconds: ") or 0)
        except ValueError:
            print("Please enter valid numbers.")
            continue

        total = hours * 3600 + minutes * 60 + seconds
        if total <= 0:
            print("Please enter a time greater than 0.")
            continue

        countdown(total)

        again = input("\nStart another timer? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
