from datetime import date

print("🎂 Age Calculator Program")
print("Enter your date of birth below (DD/MM/YYYY)\n")

try:
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

    print("\n📅 Today's Date:", today.strftime("%d %B %Y"))
    print("📆 Today is:", today.strftime("%A"))
    print("\n🎉 Your Exact Age")
    print(f"👉 {years} Years, {months} Months, {days} Days")

except ValueError:
    print("\n❌ Invalid input! Please enter a valid date.")
