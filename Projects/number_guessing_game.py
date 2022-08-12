import random
def guess_game(n):
    chances=5
    random_num = random.randint(1,n)
    guess = int(input("Enter the Number: "))
    chances=chances-1
    print(f"You have {chances} left")
    while(random_num != guess and chances!=0):
        if(guess<random_num):
            print("Number is low")
            guess = int(input("Enter the Number: "))
            chances=chances-1
            print(f"You have {chances} left")
        elif(guess>random_num) :
            print("Number is High")
            guess = int(input("Enter the Number: "))
            chances=chances-1
            print(f"You have {chances} left")
    print(f"Nice!!{random_num} is the correct answers.You had {chances} chances left")
def main():
    guess_game(20)
if __name__=="__main__":
    main()