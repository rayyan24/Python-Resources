def greet():
    print("Good Morning")
def greet0(name="bro"):
    print("Good Morning", name)
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        a = n*fact(n-1)
        return a
def add(m):
    if m == 0:
        return 0
    else:
        a = m+add(m-1)
        return a
d = add(997)
def big_finder(num1, num2, num3):
    a = [num1, num2, num3]
    a.sort()
    return a[2]
big_finder(1, 2, 3)
def c2f(c):
    f = c*(9/5)+32
    print(f)
print("Hello",end=" ")
# print("Rayyan",end=" ")
# n=6
# for i in range(n):
#     print((n-i)*"*")
def right_triange_star_pattern():
    n = 3
    for i in range(n):
        print((n-i)*"*")
right_triange_star_pattern()
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
