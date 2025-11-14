num_of_bags = int(input('PLease enter the number of bags:'))
total_income = num_of_bags * 850

if num_of_bags > 100:
    total_income += 2000
    print(f"The total income is {total_income}.00")
