user_amount = float(input('Please enter the amount you wan to send:'))

charge = 0

if user_amount <= 100:
    charge = 2
elif user_amount <= 500:
    charge = 5
elif user_amount > 500:
    charge = 10
else:
    print('You have entered an invalid amount.')        

final_amount = user_amount - charge

print(f"Amount sent: GHS{user_amount} ")
print(f"Transaction Charge: GHS{charge}")
print(f"You sent GHS{final_amount}")