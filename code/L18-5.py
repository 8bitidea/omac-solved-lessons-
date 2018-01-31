import turtle


def draw_square():
	w = turtle.Screen()
	w.bgcolor("green")
	t = turtle.Turtle()
	t.shape("turtle")
	t.speed(1)
	t.color("blue")
	t.forward(100)
	t.right(90)
	t.forward(100)
	t.right(90)
	t.forward(100)
	t.right(90)
	t.forward(100)
#	t.right(90)
	
	w.exitonclick()

draw_square()