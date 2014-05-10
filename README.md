This is my attempt to recreate the famous, "Flappy Bird" game in pygame.
###How to Play the game:
Your main objective is to get pass through the tunnels without colliding or falling down to the space. Your score increases by 1 if you pass a tunnel. And most importantly, press "Space" to flap the bird.

###Initial Thoughts for the game:
I thought of doing something new to the Flappy Bird game and so far I can only think of Flappy Bird Space. Space.jpg, Space1.jpg, Space2.jpg, Space3.jpg, Space4.jpg are the background images of the game and the images scroll along the screen as you play the game(which I think is pretty cool :D). 

I wanted to add sounds for different actions in the game, like if you collide then a particular sound and if you accelerate upwards or downwards then another sound, but I am new to Pygame and I haven't been able to figure that out yet. So, I decided to use pygame.mixer and play a music that I found online. I googled for "Space music" and I think the music that I have used blends with game.

Apart from that I wanted to do something with the tunnels as well, the standard "Flappy Bird" game has green tunnels, so I wanted to change that with something like a pile of rocks. My photoshop skills are not upto the mark to create such a texture or anything related to that. So, I ended up creating Brown-ish tunnels.

And for the bird, I wanted to use a Sprite sheet but couldn't find it online and I am not that skillful to create one on my own. So, I used the Standard Yellow bird's picture.


#The game looks like this:
![ScreenShots](https://raw.githubusercontent.com/floydutd/FlappyBird-Space/master/ScreenShots/Main-game.JPG)
![ScreenShots](https://raw.githubusercontent.com/floydutd/FlappyBird-Space/master/ScreenShots/Game-Over.JPG)



The Script may not be the best but I have tried to best so far. I know there's a lot to be added to the game and if you think you can help me with the sounds I was mentioning earlier and other stuffs that you think needs to be added to the game then PLEASE FEEL FREE TO FORK THE PROJECT AND START CONTRIBUTING. :)

#Physics for Collision
For the collision detection, I have used the basic concept of checking the distance between two objects. If the distance between the bird and the tunnel is equal to or less than the numbers I have predefined then it collides. The predefined numbes are found out by adding up the radius of the bird and half the width of the tunnel or radius of the bird and the height of the tunnel. It's not that complicated, when you go through the code you will have a better understanding of it.

Talking about the progress with the code so far:
1) The score counter  is up and running.
2) The scrolling background images works pretty good as it had been giving me a lot of trouble.
3) Now, you can restart the game after pressing "Enter". ( I believe I spent the most of my time working on this)

### All the necessary files are in the folder called "FlappyBird-Space"
