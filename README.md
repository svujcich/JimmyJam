# JimmyJam

In this terminal based python game, the player is tasked with saving Jimmy from impending death 

Jimmy was at a royal party and accidentally spilled wine on the King. The King was embarrased, Jimmy's punishment is death. To accomplish this task, the user must first engage in a game of hangman with Jimmy to brainstorm a good argument that could get him off the hook. If the player guesses the word correctly they go 
to the castle and engage in a choose your own adventure type story line. The user gains and loses points by appologizing, bluffing, and complimenting the king. If the user scores 7+ points, Jimmy is released and the player wins!

*Note that the keyword discovered during hangman is not required to win, however it has the highest point value (3 points).


![jimmyjam](https://user-images.githubusercontent.com/106559768/236706176-2c44ed72-a45e-433d-8247-a87eac886cd1.jpg)

The image above shows a high level overview of the game. On the highest level, there is a main gameplay loop. The user plays the game, either wins or loses, and the program asks the user if they want to continue playing. When the user decides they no longer wish to play, the loop breaks and the game is over. 

Inside the main gameplay loop are a set of golbal conditions which are set to false. As the user plays, if a condition is met, the condition changes to "True". The conditions are funneled through if statements to redirect the game appropriately. 

Nested inside the loop are the two core minigame loops: hangman and choose your own adventure. 

Download the code to test it out, or check out a demo [here](https://www.youtube.com/watch?v=19Vc3kKqBrg)!


