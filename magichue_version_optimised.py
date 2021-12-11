import json
import os
from requests.api import get
from websocket import create_connection
import time
import magichue
from magichue import discover_bulbs
import requests
import asyncio
import random

lastevalue = None
# print("---- \n DISCOVERING BULBS (debug lol): \n")
# print(discover_bulbs())
# print("---- \n")
leds = magichue.Light('192.168.1.154')
#print("leds are on: ",leds.on, "\n and are colored in: ", leds.rgb, "\n") # obviously another debug

if not leds.on:
    print("Lights are off, turning them on...")
    leds.on = True
    print("Leds have been turned on!")

ws = create_connection("ws://localhost:6557/socket")
print("---")
print("websocket live")
print("---")

leds.rgb = (150, 150, 150)
print("Default lights status READY! \n ----")

while True:
    result = ws.recv()
    result_dict = json.loads(result)
    #print(result_dict) # the cursed 2mb print

    if result_dict['event'] == "beatmapEvent":
            etype = result_dict['beatmapEvent']['type']
            evalue = result_dict['beatmapEvent']['value']


            # ^ of course that was something i am incapable of figuring out myself, thank you NotBlue and KickBull! 
            if etype == 1:
                
                if evalue == 0 and lastevalue != evalue: # OFF
                    lastevalue = evalue
                    #leds.on = False too slow to turn back on, bad, stinky.
                    leds.allow_fading = False
                    leds.rgb = (1,1,1)

                
                if evalue == 1 and lastevalue != evalue: # blue full
                    lastevalue = evalue
                    leds.allow_fading = False
                    leds.rgb = (0, 0, 255)


                if evalue == 2 and lastevalue != evalue: # blue, fade in
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (0, 0, 255)
    
                                
                if evalue == 3 and lastevalue != evalue: # blue, fade out
                    lastevalue = evalue
                    leds.allow_fading = True
                    #leds.rgb = (0, 0, 255)
                    leds.rgb = (0,0,100)
    

                if evalue == 5 and lastevalue != evalue: # red full
                    lastevalue = evalue
                    leds.allow_fading = False
                    leds.rgb = (255,0,0)
        

                if evalue == 6 and lastevalue != evalue: # red, fade in
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (255,0,0)
         

                if evalue == 7 and lastevalue != evalue: # red, fade out
                    lastevalue = evalue
                    leds.allow_fading = True
                    #leds.rgb = (255,0,0)
                    leds.rgb = (100,0,0)