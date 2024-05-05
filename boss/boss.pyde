x=50
y=50
w=0
s=500
n=500
a=500
g=200
k=250
l=250
def setup():
    size(500,500)
def draw():
    global x,y,w,s,n,a,g,l,k
    background(0)
    stroke(0,0,255)
    strokeWeight(10)
    point(x,y)
    point(x,y-8)

    stroke(255,0,255)
    strokeWeight(g)
    point(250,250)

    stroke(255,0,0)
    strokeWeight(30)
    line(w,s,n,a)
    
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
    if x>150 and y>150 and x<350 and y<350:
        text(u'КХррррррррррр',250, 100)
        n=n-2
        stroke(255,255,0)
        strokeWeight(30)
        point(250,250)
