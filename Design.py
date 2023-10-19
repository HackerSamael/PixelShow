import turtle
from time import sleep
t = turtle.Turtle()


def drawDot(x,y,c):
	t.penup()
	t.goto(y-150,-x+150)
	t.pendown()
	t.dot(10,c)

def find_len(s):
	r = 0
	c = 0
	i = 0

	while (s[i]!="\n"):
		r+=1
		i+=1
	c = s.count("\n")

	return r,c

with open("heart.txt", "r") as f:
	l = f.read()

fullList= []
temp= []
i = 0
j = 0

r,c = find_len(l)


for i in range(c):
	for j in range(r):
		temp.append(l[i*91+j])
	fullList.append(temp)
	temp =[]
# print(fullList)




for i in range(0,c*5,5):
	for j in range(0,r*5,5):
		if fullList[i//5][j//5] == "@":
			drawDot(i,j,"yellow")
		elif fullList[i//5][j//5] == "%":
			drawDot(i,j,"red")
		else:
			drawDot(i,j,"black")
	

sleep(5)
