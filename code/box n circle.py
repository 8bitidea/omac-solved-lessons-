
#just for fun i have a shared code from this gentleman 
# his original post in the form : 
#https://macdiscussions.udacity.com/t/draw-a-flower-using-turtle-graphics/63549
#and i mirge it with my code :D 
#i think that is beautiful <3 it 

import turtle

def draw_flower(color, bgcolor, speed):
	window = turtle.Screen()
	window.bgcolor(bgcolor)
	pen = t = turtle.Turtle()
	pen.color(color)
	pen.speed(speed)

	repeat_squares(pen, 36, 100)
	repeat_squares(pen, 36, 70)
	repeat_squares(pen, 36, 45)

	n = 360/3
	t.color("#F46A4E")
	x =0
	for c in range (n):
		x +=1
		if (x == 1): t.color("#F64A8A")
		elif(x==2): t.color("#FF4500")
		elif(x==3):
			x =0
			t.color("#F46A4E")
		t.circle(250, 60)
		t.left(120)
		t.circle(250, 60)
		t.right(120)
		t.left(3)

	turtle.write("Byte Idea")

	t.home()
	t.color("#006611")
	t.right(90)
	t.forward(500)
	window.exitonclick()

def repeat_squares(pen, n, size):
	index = 0
	while (index < n):
		draw_square(pen, size)
		index += 1

def draw_square(pen, size):
	# Starting point
	i = 0
	pen.right(100)
	while (i < 3):
		pen.forward(size)
		pen.right(90)
		i += 1
	pen.forward(size)

draw_flower("yellow", "#000000", 30)