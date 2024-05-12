x=50
y=50
def setup():
    size(500,500)
def draw():
    global x,y
    background(0)
    stroke(255,255,0)
    strokeWeight(5)
    point(x,y)
    if keyPressed==True:
        if key=='w':
            y=y-1
    if keyPressed==True:
        if key=='s':
            y=y+1
    if keyPressed==True:
        if key=='a':
            x=x-1
    if keyPressed==True:
        if key=='d':
            x=x+1

    stroke(255,0,255)
    strokeWeight(150)
    point(250,500)

    stroke(255,0,255)
    strokeWeight(20)
    point(random(0,500),random(0,500))

    
