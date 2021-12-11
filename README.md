# MagicHome LED script for BeatSaber
**Big, fat thanks to [NotBlue](https://github.com/NotBlue-Dev) and KickBull for enduring this absolute unit of a code.**

## What is this?
After seeing what NotBlue did with his fancy lights, i decided to try to make my poor gamer lights set work. I guess this time it turned out a success.
Basically some lights ingame will happen in your room if you have MagicHome compatible LEDs. _I currently do not have plans to make this nor the file any easier to read._

>[little demo (video)](https://youtu.be/uQJ527UfYaA)

## Why exactly "optimised" in the name?
Oh my dear sunshine, you don't want to receive the amount of bytes that poor LED controller received in the first tests. Even currently it's not ideal, but it works.

## How to set it up?
Haha...so...
* Get yourself [magichue-py package](https://github.com/namacha/python-magichue)
* Find a way to get your lights local IP address, there is a way mentioned in the above package github page
* Edit my script so the leds IP matches yours, shouldn't be too hard and can be done with good 'ole notepad
* Run the .py file AFTER opening Beat Saber (if it's closed prior to launching this script or closed in the process, it will error)
* Honestly just hope that this will work.

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