litres = float(input('Please enter the number of litres you want:'))
cost_per_litre = 12.50
total_cost = litres * cost_per_litre

if litres > 50:
    discount = (5/100) * total_cost 
    new_total = total_cost - discount
    print(f"Your total cost is {new_total} .")
else:
    discount = 0
    print(f"You total cost is {total_cost} .")    





