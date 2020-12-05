import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def click(key):
    pyautogui.keyDown(key)
    return
def ss():
    for i in range(460, 600):
        for j in range(160,220):
            data[i, j] = 255
    for i in range(460, 600):
        for j in range(160,220):
            data[i,j] = 200
    image.show()
    return

def isCollision(data):
# Check colison for birds
 #
 # Check colison for cactus
    for i in range(460, 600):
        for j in range(220,260):
            if data[i, j] > 100:
                click("up")
                return
    for i in range(460, 600):
        for j in range(160,220):
            if data[i, j] > 100:
                click("down")
                return

if __name__ == "__main__":
    time.sleep(5)
    click('up') 
    flag = 1
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
        if flag == 1:
        	ss()
        	flag = 0

#for i in range(200,260):
        #for j in range(550,590):