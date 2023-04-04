import pyxel

pyxel.init(80,64,title="janken game")
pyxel.load("janken_draw.pyxres")
pyxel.mouse(True)

hand_width=16
hand_height=16

com_hand = 0
#initialize variable of com hand

status = 0
#initialize variable of status of the one before clicking and after clicking

def update():

    global com_hand,status
    if status == 0:

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            com_hand = pyxel.rndi(0,2) #hand is chosen by clicking
            status = 1

        else:
            #Before clicking, randome change keep going
            com_hand = int(pyxel.frame_count / 5) % 3

    elif status == 1:
        pass #nothig done yet

    return

def draw():
    pyxel.cls(0)

    #Draw hand of CPU
    pyxel.text(4,10,"COM",7)
    pyxel.blt(32,0,0,com_hand*16,0,hand_width,hand_height,0)

    #Draw hand of player
    pyxel.text(4,32,"YOU",7)
    pyxel.blt(16,32,0,0,0,hand_width,hand_height,0)
    pyxel.blt(32,32,0,16,0,hand_width,hand_height,0)
    pyxel.blt(48,32,0,32,0,hand_width,hand_height,0)

    return

pyxel.run(update, draw)
