# try:
#     a="1.txt"
#     with open(a,"r") as a:
#         a=a.read()
# except Exception as e:
#     print(f"{a} is not present")

# try:
#     a="2.txt"
#     with open(a,"r") as a:
#         a=a.read()
#         print(a)
# except Exception as e:
#     print(f"{a} is not present")

# try:
#     a="3.txt"
#     with open(a,"r") as a:
#         a=a.read()
#         print(a)
# except Exception as e:
#     print(f"{a} is not present")
# ------------------------------------------------------
def file_read(filename):
    try:
        with open(filename, "r") as a:
            a = a.read()
            print(a)
    except Exception as e:
        print(f"{filename} not found ")


# a = input("enter file name to open: ")

file_read(input())
