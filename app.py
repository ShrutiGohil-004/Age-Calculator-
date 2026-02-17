from datetime import date


def calculate_age(birth_date, today):
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    print("🎂 Age Calculator Program")

    while True:
        try:
            print("\nEnter your date of birth (DD/MM/YYYY)")
            day = int(input("Day (DD): "))
            month = int(input("Month (MM): "))
            year = int(input("Year (YYYY): "))

            birth_date = date(year, month, day)
            today = date.today()

            if birth_date > today:
                print("❌ Birth date cannot be in the future.")
                continue

            years, months, days = calculate_age(birth_date, today)

            print("\n📅 Today:", today.strftime("%d %B %Y"))
            print("📆 Day:", today.strftime("%A"))
            print(f"🎉 Your Age: {years} Years, {months} Months, {days} Days")

        except ValueError:
            print("❌ Invalid input. Please enter a valid date.")

        choice = input("\nCalculate again? (yes/no): ").lower()
        if choice != "yes":
            print("👋 Thank you for using Age Calculator")
            break


if __name__ == "__main__":
    main()
