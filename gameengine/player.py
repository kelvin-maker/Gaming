import numpy as np
from matplotlib import pyplot as plt
import keyboard 


class Drawplayer:
    def __init__(self, posx, posy, rot):
        self.mapa =[[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,1,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]]

        self.posx = posx
        self.posy = posy
        self.rot = rot

        self.posx, self.posy = (1,1)
        self.exitx, self.exity = (3,3)
        self.rot = np.pi/4 
        
    def Mainloop(self):

        while True:
            for i in range(60):
                rot_i = rot + np.deg2rad(i - 30)
                x, y = (self.posx, self.posy)
                sin, cos = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i))
                n = 0

                while True:
                    x, y = (x + cos, y + sin)
                    n = n+1  
                    if self.mapa[int(x)][int(y)] != 0:
                        h = 1/(0.02 * n)
                        break
                plt.vlines(i, -h, h, lw =8) 

            plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
            plt.draw(); plt.pause(0.0001); plt.clf()

            key = keyboard.read_key()
            x, y = (self.posx, self.posy)

            if key == 'up':
                x, y = (x - 0.3*np.cos(rot), y + 0.3*np.cos(rot))
            elif key == 'down':
                x, y = (x- 0.3*np.cos(rot), y - 0.3*np.cos(rot))
            elif key == 'left':
                rot = rot - np.pi/8
            elif key == 'right':
                rot = rot + np.pi/8
            elif key == 'esc':
                break 

            if self.mapa[int(x)][int(y)] == 0:
                if int(self.posx) == self.exitx and int(self.posy) == self.exity:
                    break
                self.posx, self.posy = (x, y)
            plt.close()
print(Drawplayer().Mainloop(1,1))
            