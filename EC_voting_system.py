full_name = input('Please enter your fullname:').title()
age = int(input('Please enter your age:'))
nationality = input('Please enter your nationality:').lower()

if age >= 18 and nationality == 'ghanaian':
    print(f"{full_name} is eligible to vote.")
else:
    print(f"{full_name} is not eligible to vote.")    