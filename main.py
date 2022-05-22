from gameengine import *
    

gameengine = GameEngine(title= "GameEngine!", width = 800, height = 600, bg_color= (0, 0, 0, 255))

entity = Entity(gameengine, width = 50, height = 50,  x = 0, y = 0)

walls = Walls(gameengine, width = 800, height = 50,  x = 0, y = 0)

entity.center()

@gameengine.draw
def  map():
    walls.map()

gameengine.loop()
