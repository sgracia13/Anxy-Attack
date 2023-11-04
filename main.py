#Start of new python game

#Find a new sprite to use
#The sprite being utilized right now is way too small and is barely visible.
#Not a sprite that fits the theme either
hero = Actor('hero')
hero.pos = 100, 56

WIDTH = 500
HEIGHT = hero.height + 50

def draw():
    screen.clear()
    hero.draw()

hero.topright = 0,10

def update():
    hero.left += 2
    if hero.left > WIDTH:
        hero.right = 0

        

def on_mouse_down(pos):
        if hero.collidepoint(pos):
                print("EEEEEK!")
        else:
            print("You missed me!")
