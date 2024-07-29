print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
word1 = "true"
word2 = "love"
count1 = 0
count2 = 0
combined_name = name1.lower() + name2.lower()
for letter in combined_name: 
    if letter in word1: 
        count1 += 1 
    if letter in word2: 
        count2 += 1
score = int(str(count1) + str(count2))
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
