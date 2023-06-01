import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

	
    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        #reset
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
    elif letter == "C":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.pd()
        tur.left(90)
        tur.fd(20)
        #reset
        tur.pu()
        tur.right(90)
        tur.fd(10)
        tur.right(90)
        tur.fd(40)
    elif letter == "D":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(135)
        tur.fd(15)
        tur.left(45)
        tur.fd(11)
        tur.left(45)
        tur.fd(15)
        #reset
        tur.pu()
        tur.right(135)
        tur.fd(40)
    elif letter == "E":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(15)
        tur.pd()
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        #reset
        tur.pu()
        tur.left(90)
        tur.fd(10)
        tur.right(90)
        tur.fd(25)
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.left(90)
        tur.fd(25)
        tur.right(135)
        tur.fd(40)
        tur.left(135)
        tur.fd(25)
        #reset
        tur.pu()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(15)		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
