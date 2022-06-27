import pyautogui
import time
import random

time.sleep(5)

while True:
    o = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    o0 = random.choice(o)
    o1 = random.choice(o)
    o2 = random.choice(o)
    o3 = random.choice(o)
    o4 = random.choice(o)
    o5 = random.choice(o)
    o6 = random.choice(o)
    o7 = random.choice(o)
    pyautogui.write(o0 + o1 + o2 + o3 + o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7 + o4 + o5 + o6 + o7 + '\n')
