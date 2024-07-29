print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
size_costs = {'S': 15, 'M': 20, 'L': 25}
pepperoni_cost = 2 if size == 'S' else 3
cheese_cost = 1

if size in size_costs:
  base_cost = size_costs[size]
else:
  raise ValueError("Invalid pizza size. Choose either 'S', 'M', or 'L'.")

final_cost = base_cost
if add_pepperoni == "Y":
  final_cost += pepperoni_cost
else:
  final_cost += 0
if extra_cheese == "Y":
  final_cost += cheese_cost
else:
  final_cost += 0

print(f"Your final bill is: ${final_cost}.")
