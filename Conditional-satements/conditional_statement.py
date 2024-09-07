# There are mainly three types of coondtional statements in python:
# 1. if
# 2. if - else
# 3. if - elif - else

x = 1

if x % 2 == 0 and x > 3:
    print("yes, and its even")
elif x % 2 != 0 and x > 3:
    print("Yes but odd")
elif x % 2 == 0 and x < 3:
    print("no but even")
else:
    print("not even not greater")

