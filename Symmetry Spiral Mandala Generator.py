import turtle
import colorsys

# ---------------- SETUP ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Allow RGB colors
turtle.colormode(1)

# ---------------- ART FUNCTION ----------------
def draw_mandala(circles, radius, rotation_step):
    hue = 0

    for i in range(circles):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        pen.pencolor(color)

        pen.circle(radius)
        pen.left(rotation_step)

        hue += 1 / circles

# ---------------- DRAW PATTERN ----------------
draw_mandala(
    circles=180,       # more = more detail
    radius=200,
    rotation_step=5    # smaller = tighter spiral
)

turtle.done()
