#Love calculator program
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combined = name1 + name2

t = name_combined.lower().count("t")
r = name_combined.lower().count("r")
u = name_combined.lower().count("u")
e = name_combined.lower().count("e")

#count how many "true" alphabets count on the name1 and name2
true = t + r + u + e


l = name_combined.lower().count("l")
o = name_combined.lower().count("o")
v = name_combined.lower().count("v")
e = name_combined.lower().count("e")

#count how many "love" alphabets count on the name1 and name2
love = l + o + v + e

#total count true and love
love_score = int(f"{true}{love}")

if (love_score <= 10) or (love_score >= 90):
  print(f"Your score is {love_score}, you go together like coke and mentos🌋")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together💑")
else:
  print(f"Your score is {love_score}, just fine😬")




