print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
p = lower_case_string.count("p")
r = lower_case_string.count("r")
i = lower_case_string.count("i")
y = lower_case_string.count("y")
a = lower_case_string.count("a")
n = lower_case_string.count("n")
k = lower_case_string.count("k") 
a = lower_case_string.count("a")
                          
priyanka = p + r + i + y + a + n + k + a

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("v")

love = l + o + v + e
love_score = int(str(priyanka) + str(love))
print(love_score)
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score},you are like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"your score is {love_score},you are good together")
else:
  print(f"your score is {love_score}")