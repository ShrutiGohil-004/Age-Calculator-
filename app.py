from datetime import date

print("🎂 Age Calculator Program")

# User input
birth_day = int(input("Enter birth day (DD): "))
birth_month = int(input("Enter birth month (MM): "))
birth_year = int(input("Enter birth year (YYYY): "))

# Today's date
today = date.today()

# Birth date object
birth_date = date(birth_year, birth_month, birth_day)

# Calculate age
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

# Output
print("\n📅 Today's Date:", today.strftime("%d %B %Y"))
print("📆 Day:", today.strftime("%A"))

print("\n🎉 Your Age Is:")
print(f"👉 {years} Years, {months} Months, {days} Days")
