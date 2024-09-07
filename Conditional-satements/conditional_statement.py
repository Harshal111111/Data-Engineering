# There are mainly three types of coondtional statements in python:
# 1. if
# 2. if - else
# 3. if - elif - else

x = 1

if x % 2 == 0 and x > 3:
    print("yes, and its prime")
elif x % 2 != 0 and x > 3:
    print("Yes but not prime")
elif x % 2 == 0 and x < 3:
    print("no but prime")
else:
    print("not prime not greater")