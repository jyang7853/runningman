from gamelib import *

game = Game(800,400,"Shooter")
bk = Image("images//background.jpg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

title = Image("images//startlogo.png",game)
bk.draw()
title.draw()
game.drawText("RUNNING MAN",370,40)
game.drawText("Controls",380, 280)
game.drawText("[ARROW KEYS] to move",320, 310)
game.drawText("[SPACE] to jump",345, 330)
game.drawText("Press [SPACE] to Begin",600, 370)
game.drawText("OBJECTIVE: Collect 10 coins to win!",270, 350)
game.drawText("DODGE THE ASTEROIDS!",310, 370)
game.update(1)
game.wait(K_SPACE)

runningman = Animation("images//runningman.png",12,game,1240/3,1292/4)
runningman.moveTo(400,315)
runningman.resizeTo(200,140)
runningman.stop()

asteroid = Animation("images//asteroid2.png", 30, game, 32, 32, 1)
x = randint(50, 590)
y = -100
asteroid.moveTo(x, y)
asteroid.setSpeed(5, 180)

platform = Image("images//platform.png",game)
platform.setSpeed(4,90)

ring = Animation("images\\ring2.png",64,game,64,64,1)
ring.resizeBy(-50)
y = randint(100,400)
ring.moveTo(game.width+100,y)
ring.setSpeed(5, 90)

jumping = False
landed = False
factor = 1

gameover = Image("images//gameoverlogo.jpg",game)
gameover.resizeTo(800, 400)

while not game.over:
    game.processInput()

    game.scrollBackground("left", 2)
    asteroid.move()
    bk.draw()
    runningman.draw()
    platform.move()
    ring.move()
    if platform.isOffScreen("left"):
        platform.moveTo(game.width,randint(250,350))

    if keys.Pressed[K_LEFT]:
        runningman.nextFrame()
        runningman.x -= 6
    elif keys.Pressed[K_RIGHT]:
        runningman.prevFrame()
        runningman.x += 6
    else:
        runningman.draw()

    if asteroid.isOffScreen("bottom"):
        x = randint(50, 590)
        y = -100
        asteroid.moveTo(x, y)
        asteroid.speed += 0.3  # 

    if runningman.collidedWith(ring):
        y = randint(100,400)
        ring.moveTo(game.width+100,y)
        game.score += 1

    if ring.isOffScreen("left"):
        y = randint(100,300)
        ring.moveTo(game.width+100,y)
        
    if runningman.y < 315:
        landed = False
        if runningman.collidedWith(platform,"rectangle"):
            landed = True

    else:
        landed = True

    if jumping:
        runningman.y -= 20 * factor
        factor *= .95
        landed = False
        if factor < .18:
            jumping = False
            factor = 1

    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True

    if not landed:
        runningman.y += 6
        
    if game.score > 9:
        gameover = Image("images//youwin.jpg",game)
        game.drawText("YOU WIN!",380, 280)
        gameover.resizeTo(800, 400)
        game.over = True
         
    if runningman.collidedWith(asteroid):  #
        game.over = True

    game.displayScore()
    game.update(60)
gameover.draw()
game.drawText("Press [SPACE] to Exit",400, 320)
game.update(1)
game.wait(K_SPACE)
game.quit()  
