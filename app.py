print("🎂 Age Calculator Program")

birth_year = input("Enter your birth year: ")
current_year = input("Enter current year: ")

if not birth_year.isdigit() or not current_year.isdigit():
    print("❌ Please enter valid numeric values only")
else:
    birth_year = int(birth_year)
    current_year = int(current_year)

    if birth_year > current_year:
        print("❌ Birth year cannot be greater than current year")
    else:
        age = current_year - birth_year
        print(f"✅ Your age is: {age} years")
