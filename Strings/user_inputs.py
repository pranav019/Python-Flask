size_input = input("Enter your house size (in sq feet): ")
sq_feet = int(size_input)

sq_meters = sq_feet / 10.8
print(f"{sq_feet} sq feet is {sq_meters: .3f} in sq_meters")
