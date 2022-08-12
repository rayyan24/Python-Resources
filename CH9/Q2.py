def game():
    a=str(99)
    return a
score=game()
a=open("SCORE.txt","r")
c=a.read()
a.close()
if c=="":
    b=open("SCORE.txt","w")
    b.write(score)
    b.close()
if score>c:
    b=open("SCORE.txt","w")
    b.write(score)
    b.close()



