from datetime import date

print("🎂 Age Calculator Program")

while True:
    try:
        print("\nEnter your date of birth (DD/MM/YYYY)")
        birth_day = int(input("Day (DD): "))
        birth_month = int(input("Month (MM): "))
        birth_year = int(input("Year (YYYY): "))

        birth_date = date(birth_year, birth_month, birth_day)
        today = date.today()

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += 30

        if months < 0:
            years -= 1
            months += 12

        print("\n📅 Today:", today.strftime("%d %B %Y"))
        print("📆 Day:", today.strftime("%A"))
        print(f"🎉 Your Age: {years} Years, {months} Months, {days} Days")

    except ValueError:
        print("❌ Invalid date. Try again.")

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("👋 Thank you for using Age Calculator")
        break
