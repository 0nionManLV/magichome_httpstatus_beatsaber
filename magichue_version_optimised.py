import json
from requests.api import get
from websocket import create_connection
import magichue


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
print("Default lights READY!\n----")

while True:
    result = ws.recv()
    result_dict = json.loads(result)
    #print(result_dict) # the cursed 2mb print

    # Limiting packet rates would be nice. The below block of code does function..sort of. Rather keep it commented out for now.
    # The prints should be self explanatory on what each of them does.
    # It fired 'paused' and 'unpaused' event mid-song, therefore i sent this functionality to the shadow realm.

    # if result_dict['event'] == "songStart":
    #     print("^^^ SONG STARTED ^^^")
    #     leds.rgb = (0,0,0)
    
    # if result_dict['event'] == 'finished':
    #     print("^ Level cleared, good job! ^")
    #     leds.rgb = (100, 150, 100)

    # if result_dict['event'] == 'failed':
    #     print("___ LEVEL FAILED ___")
    #     leds.rgb = (150,100,100)

    # if result_dict['event'] == 'menu':
    #     print("Returning to menu...")
    #     leds.rgb = (150,150,150)

    # if result_dict['event'] == 'pause':
    #     print("PAUSED")
    #     leds.rgb = (50,50,50)
    
    # if result_dict['event'] == 'resume':
    #     print("UNPAUSED")
    #     leds.rgb = (0,0,0)

    # I don't reccomend commenting out anything below this line, above is fine.


    if result_dict['event'] == "beatmapEvent":
            etype = result_dict['beatmapEvent']['type']
            evalue = result_dict['beatmapEvent']['value']
            # ^ of course that was something i am incapable of figuring out myself, thank you NotBlue and KickBull! 

            if etype == 1: # before - type 1(ring lights) ; 4 (road lights), seems like ring ones work a bit better.
                
                if evalue == 0 and lastevalue != evalue: # OFF
                    print("OFF")
                    lastevalue = evalue
                    #leds.on = False # too slow to turn back on, bad, stinky.
                    leds.allow_fading = False
                    leds.rgb = (0,0,0)

                
                if evalue == 1 and lastevalue != evalue: # blue full
                    print("Blue full")
                    lastevalue = evalue
                    leds.allow_fading = False
                    leds.rgb = (0, 0, 255)


                if evalue == 2 and lastevalue != evalue: # blue, fade in
                    print("Blue, fade in")
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (0, 0, 255)
    
                                
                if evalue == 3 and lastevalue != evalue: # blue, fade out
                    print("Blue, fade out")
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (0, 0, 255) # this originally was commented out, enabled for the greater good of immersion effect.
                    leds.rgb = (0,0,55) # 55
    

                if evalue == 5 and lastevalue != evalue: # red full
                    print("Red full")
                    lastevalue = evalue
                    leds.allow_fading = False
                    leds.rgb = (255,0,0)
        

                if evalue == 6 and lastevalue != evalue: # red, fade in
                    print("Red, fade in")
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (255,0,0)
         

                if evalue == 7 and lastevalue != evalue: # red, fade out
                    print("Red, fade out")
                    lastevalue = evalue
                    leds.allow_fading = True
                    leds.rgb = (255,0,0) # this originally was commented out, enabled for the greater good of immersion effect.
                    leds.rgb = (55,0,0) # 55