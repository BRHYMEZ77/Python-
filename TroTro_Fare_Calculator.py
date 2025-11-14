user_route = input('Please enter your route(Madina or Tema or Kasoa):').title()
num_of_passengers = int(input('Please enter the number of passengers:'))

fare = 0

if user_route == 'Madina':
    fare = 5
elif user_route == 'Tema':
    fare = 8    
elif user_route == 'Kasoa':
    fare = 10
else:
    print('You have entered the wrong route.')

total_fare = fare * num_of_passengers
print(f"The total fare is GHC{fare * num_of_passengers}.00")    