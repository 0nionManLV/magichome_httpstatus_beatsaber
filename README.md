# MagicHome LED script for BeatSaber
**Big, fat thanks to [NotBlue](https://github.com/NotBlue-Dev) and KickBull for enduring this absolute unit of a code.**

## What is this?
After seeing what NotBlue did with his fancy lights, i decided to try to make my poor gamer lights set work. I guess this time it turned out a success.
Basically some lights ingame will happen in your room if you have MagicHome compatible LEDs. _I currently do not have plans to make this nor the file any easier to read._

>[gameplay demo](https://youtu.be/uQJ527UfYaA)
>[visual demo](https://youtu.be/0tTJZcoz2fY)

## Why exactly "optimised" in the name?
Oh my dear sunshine, you don't want to receive the amount of bytes that poor LED controller received in the first tests. Even currently it's not ideal, but it works.

## "Technicolor" version???
Yeah, well not quite but yeah. Gotta love the random colors Technicolor mod brings to the game so tried to bring it to life aswell. Colors are not synced with the game itself as i am incapable of even making the original version work by myself.
All credits for inspiration go to [Technicolor mod](https://github.com/Aeroluna/Technicolor). The lights might not be as flashy as one would expect due to a check for repeating events. (if mapper placed flash event twice in row, without off event in middle, the leds will only "flash" once, applies to original version too.)

If you compare this to the actual mod, pretend it's set to "warm/cold" and highest lights frequency.

After sitting and looking at flashing lights for a few minutes, i'd personally suggest the original version for the time being, however don't be shy to test the "flashier" version.

## How to set it up?
Haha...so...
* Get yourself [magichue-py package](https://github.com/namacha/python-magichue)
* Find a way to get your lights local IP address, there is a way mentioned in the above package github page
* Edit my script so the leds IP matches yours, shouldn't be too hard and can be done with good 'ole notepad
* Run the .py file AFTER opening Beat Saber (if it's closed prior to launching this script or closed in the process, it will error)
* Honestly just hope that this will work.

## The ugly
So main _ugly_ is the packet rates. Most of stuff i tested is just too flashy and the lights can only do so many updates per second. Unless i upgrade to some custom microcontroller solution, this will be the best it can get. Disabling fades is not worth the "immersion" loss as with the delay they add this does look better than just red/blue/off.

It controls all the strip at once. I've never had individually programmable leds but if i ever get my hands on such, i might try to do something.

Repeating events like multiple fades in row are ignored due to the built in "packet limiter". You really don't want to accidentally dos attack your weak lights controller with hundreds of updates per second.

Another _ugly_ is this readme, deal with it. 8)

## Requirements
1. [magichue-py package](https://github.com/namacha/python-magichue) | pip install magichue-python
2. pip install websocket (probably not a default install)
3. pip install requests (probably not default aswell)
4. pip install json (more likely to be a default but i'll list it anyways)

## Sources
- The legend who created a magichome API that can actually flash lights instead of only fading - https://github.com/namacha/python-magichue
- The legend whose adventure started by me messaging him about an issue i had with my previous lights project. He pretty much made this a real thing in the end - [NotBlue](https://github.com/NotBlue-Dev)
- Google, duuh
- KickBull, the python wizard who helped me understand json formatting and websockets a tad bit better.