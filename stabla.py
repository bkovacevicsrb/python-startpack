import turtle

t = turtle.Turtle()

t.color("green")
t.left(90)
t.backward(150)
t.speed(10)


najkraca = 10
ugao = 15.0
procenatGrane = 0.7

def grana(n):
    if n >= najkraca:
        t.forward(n)

        t.right(ugao)
        grana( n*procenatGrane * 0.8 )

        t.left(ugao)
        grana( n*procenatGrane )

        t.left(ugao)
        grana( n*procenatGrane* 0.8 )

        t.right(ugao)
        t.backward(n)


grana(150)
