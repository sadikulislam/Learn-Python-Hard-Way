# more variable and printing
name = 'Max'
age = 27
height = 5.9 # feet
weight = 175 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Brown'
height_in_centimeter = 30.48 * height # convert height in centimeter
weight_in_kg = 0.453592 * weight # convert weight in kg

print(f"Lets talk about {name}.")
print(f"He is {height} feet tall.")
print(f"He is {weight} kg.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth is usually {teeth} depending on the coffee.")

total = age + height_in_centimeter + weight_in_kg

print(f"If I add {age}, {round(height_in_centimeter)}, {round(weight_in_kg)} I got {round(total)}")