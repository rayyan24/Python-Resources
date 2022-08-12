import random
def rockPaperScissors():
    print("Enter r for rock p for paper s for scissors")
    user=input()
    computer=random.choice(['r','p','s'])
    if(user==computer):
        print("Its a Tie")
    elif((user=="r" and computer=="s") or (user=="p" and computer=="r") or (user=="s" and computer=="p")):
        print("You Won")
    else:
        print("You Lost")
def main():
    rockPaperScissors()
if __name__=="__main__":
    main()