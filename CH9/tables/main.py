

# for i in range(2,21):
#     with open(f"table_of_{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}x{j}={i*j}\n")


for i in range(2,21):
    f=open(f"table_of_{i}.txt","w")
    for j in range(1,11):
        f.write(f"{i}x{j}={i*j}\n")
    f.close()
