  Hello everyone, my name is Alex and I've been setting up an unofficial
repository for a side project that I've been working on yesterday related to
Monday's club meeting. It's regarding a Python based game that is made from
scratch (less PyGame for image processing). We talked about making a side
scroller game, such as Super Mario Bros. clone and a chess board game as ideas.
I've gone ahead and started the side scroller, but have used Mega Man as the
player character instead of Mario for the proof of concept.

  If anyone is interested in programming and likes solving problems from scratch
using the concepts we've learned in class, feel free to join me as I continue to
work on the side scroller and possibly start working on the chess game as well.
The framework/library/module, PyGame, is discussed in our CSC Intro Programming
textbook and will be covered during the course. This project will help you gain
additional practice outside of class if you need it and I am more than happy to
answer any of your questions as they relate to the project. Working on this
project will help you with Assignment: Program 03 and your Final.

  The side scroller won't strictly be Mega Man per se, I am mainly using sprites
that already exist so that I can focus on the programming concepts without being
distracted by other areas of game design. Elements from Mario, Metroid etc can
and will be added as programming challenges using whatever sprites as place
holders.

![Alt text](https://github.com/SecretKosmoNaut/MCGDC/blob/master/megaman/preview/11.3.17.2:20.gif)

  11.5.17 - Add Jumping Functionality [WIP]

    f(x)=-1/ba^2(x-[b*a+c])^2+b

* a = momentum percent
* b = maximum height
* b * 2 = maximum distance
* c = starting x-position
* x = current x-position

  Started working on the game's jumping physics. It originally started as an
equation with hard-coded variables that couldn't take into account the
possibility of implementing momentum but I figured out a pattern that yields
an equation that works. This equation yields one x-intercept centered at the
origin (0,0) and can be offset by the player's x-position within the game making
it perfect for use in games. The sprite currently used is 32x32 pixels, so I set
the jump height to 64px and the maximum jump distance to 128px (dependent on
momentum). Below are four parabolas set at 100%, 75%, 50% and 25% of the
maximum moment the player will be able to generate running to show how the
function works.

![Alt text](https://raw.githubusercontent.com/SecretKosmoNaut/MCGDC/master/megaman/preview/jumping_function.png)

  11.6.17 - Jumping [WIP]

  ![Alt text](https://github.com/SecretKosmoNaut/MCGDC/blob/master/megaman/preview/11.6.17.gif)


  11.7.17 - Jumping Fixes [WIP]

  Fixed:
  * Directional changes mid-air causing player to halt jumping and glide in the air
  * Directional changes mid-air causing player to fall through the floor upon "landing"
  * Not being able to initiate a jump while running "gliding on the floor"

  ![Alt text](https://github.com/SecretKosmoNaut/MCGDC/blob/master/megaman/preview/11.7.17.gif)

  Requirement(s):
* PyGame - https://www.pygame.org/wiki/GettingStarted

  To Run:
* python megaman.py

  To-Do:
* Add jumping module [WIP]
* Re-Structure animation module
* Fix multi-jump bug
* Add platform
* Add collision module/implementation
