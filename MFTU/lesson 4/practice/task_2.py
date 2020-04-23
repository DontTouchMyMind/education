import graphics as gr

window = gr.GraphWin("my_home", 600, 600)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(600, 300))
    sky.setFill('blue')
    sky.draw(window)


def draw_earth():
    earth = gr.Rectangle(gr.Point(0, 300), gr.Point(600, 600))
    earth.setFill('dark grey')
    earth.draw(window)


def draw_cloud1():
    cloud1 = gr.Circle(gr.Point(50, 50), 15)
    cloud1.setFill('white')
    cloud2 = gr.Circle(gr.Point(65, 50), 15)
    cloud2.setFill('white')
    cloud3 = gr.Circle(gr.Point(80, 50), 15)
    cloud3.setFill('white')
    cloud4 = gr.Circle(gr.Point(55, 60), 15)
    cloud4.setFill('white')
    cloud5 = gr.Circle(gr.Point(70, 60), 15)
    cloud5.setFill('white')
    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)


def draw_cloud2():
    cloud1 = gr.Circle(gr.Point(350, 150), 17)
    cloud1.setFill('white')
    cloud2 = gr.Circle(gr.Point(365, 150), 19)
    cloud2.setFill('white')
    cloud3 = gr.Circle(gr.Point(380, 150), 15)
    cloud3.setFill('white')
    cloud4 = gr.Circle(gr.Point(355, 160), 13)
    cloud4.setFill('white')
    cloud5 = gr.Circle(gr.Point(370, 160), 17)
    cloud5.setFill('white')
    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)


def draw_cloud3():
    cloud1 = gr.Circle(gr.Point(450, 80), 20)
    cloud1.setFill('white')
    cloud2 = gr.Circle(gr.Point(485, 75), 23)
    cloud2.setFill('white')
    cloud3 = gr.Circle(gr.Point(510, 70), 21)
    cloud3.setFill('white')
    cloud4 = gr.Circle(gr.Point(460, 95), 19)
    cloud4.setFill('white')
    cloud5 = gr.Circle(gr.Point(485, 98), 21)
    cloud5.setFill('white')
    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)


def draw_sun():
    sun = gr.Circle(gr.Point(80, 80), 35)
    sun.setFill('yellow')
    sun.draw(window)


def draw_house():
    house = gr.Rectangle(gr.Point(425, 325), gr.Point(575, 475))
    house.setFill('grey')
    house.setWidth(5)
    roof = gr.Polygon(gr.Point(425, 325), gr.Point(500, 270), gr.Point(575, 325))
    roof.setFill('brown')
    roof.setWidth(5)
    win1 = gr.Rectangle(gr.Point(465, 365), gr.Point(500, 400))
    win1.setFill('yellow')
    win1.setWidth(5)
    win2 = gr.Rectangle(gr.Point(500, 365), gr.Point(535, 400))
    win2.setFill('yellow')
    win2.setWidth(5)
    win3 = gr.Rectangle(gr.Point(465, 400), gr.Point(500, 435))
    win3.setFill('yellow')
    win3.setWidth(5)
    win4 = gr.Rectangle(gr.Point(500, 400), gr.Point(535, 435))
    win4.setFill('yellow')
    win4.setWidth(5)
    house.draw(window)
    roof.draw(window)
    win1.draw(window)
    win2.draw(window)
    win3.draw(window)
    win4.draw(window)


def draw_tree():
    tree1 = gr.Polygon(gr.Point(200, 550), gr.Point(250, 500), gr.Point(300, 550))
    tree1.setFill('green')
    tree1.setWidth(3)
    tree2 = gr.Polygon(gr.Point(200, 525), gr.Point(250, 475), gr.Point(300, 525))
    tree2.setFill('green')
    tree2.setWidth(3)
    tree3 = gr.Polygon(gr.Point(200, 500), gr.Point(250, 450), gr.Point(300, 500))
    tree3.setFill('green')
    tree3.setWidth(3)
    tree4 = gr.Rectangle(gr.Point(245, 550), gr.Point(255, 590))
    tree4.setFill('brown')
    tree4.setWidth(3)
    tree1.draw(window)
    tree2.draw(window)
    tree3.draw(window)
    tree4.draw(window)


draw_sky()
draw_earth()
draw_sun()
draw_cloud1()
draw_cloud2()
draw_cloud3()
draw_house()

draw_tree()

window.getMouse()
window.close()
