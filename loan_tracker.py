savings = { 'Akosua': 200, 'Ama': 150, 'Adwoa': 300 }

print('Women savings:')
for name, amount in savings.items():
    print(f"{name}: GHS {amount}")

woman = input("Please enter the name of the woman to update: ").title()
new_amount = float(input("Please enter new savings amount: "))

savings[woman] = new_amount

print('New savings:')
for name, amount in savings.items():
    print(f"{name}: GHS {amount}")

