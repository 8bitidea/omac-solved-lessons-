import turtle

def flower (t):
	n = 360/3
	for c in range (n):
		t.circle(100, 60)
		t.left(120)
		t.circle(100, 60)
		t.right(120)
		t.left(3)
	t.home()
	t.color("#006611")
	t.right(90)
	t.forward(500)
		





def init ():
	w = turtle.Screen()
	w.bgcolor("#00AAE4")
	t = turtle.Turtle()
	t.shape("turtle")
	t.speed(20)
	t.color("#F46A4E")
	flower(t)
	w.exitonclick()



init()
