# 2048
### Description
The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048 (in default case). 

Here is a Python version of the game.

![board](https://user-images.githubusercontent.com/63636498/82175845-acfd2400-98f2-11ea-91bc-799cb63c715c.JPG)

***Note : My program is made to work in Ubuntu based environments. Avoid using it on Wndows***

There are two files `2048.py` which is like the main program and `essentials.py` which contains user defined functions used for implementation of the program.

### Beginnig the Game
The program reads command line arguments as input

`python 2048.py --size <board dimensions> --win <max value>`

or 

`python 2048.py -n <board dimensions> -w <max value>`

If no arguments are passed `python 2048.py` then the board dimension are set to 5 x 5 and the winning criteria is set to no. 2048

If the entered value for win is not a power of 2 then it will rounded to lowest power of 2 greater than or equal to win.  Eg: `python 2048.py -w 476` then `Win criteria is 512`

The Game starts with two 2's at random position.

### Moves
 * Use WASD keys to controls the moves. (Both upper and lower case can be used)
 
   ![keys](https://user-images.githubusercontent.com/63636498/82177678-e1271380-98f7-11ea-8e0b-121894136767.png)

* A move is said to be invalid if none of the number is able to move.Eg:

  ![image](https://user-images.githubusercontent.com/63636498/82178106-d4ef8600-98f8-11ea-8619-8f2ccd089646.png)

    Here moves `w` and `a` are invalid

* After each valid move, a number `2` is randomly inserted in an empty position

### Ending 
* The Game ends if the win number is created. Hence you win the game.

  ![image](https://user-images.githubusercontent.com/63636498/82178809-7f1bdd80-98fa-11ea-8adb-3454632b942b.png)


* Else if no possible moves are left the Game ends. Hence you lose the game.

  ![image](https://user-images.githubusercontent.com/63636498/82180973-3adf0c00-98ff-11ea-974a-105e1a1f2d83.png)

* If you want to quit in the middle of the Game press `q`or `Q`. 
 You will be prompted : `Do you want to Exit the game ?`
 
   ![image](https://user-images.githubusercontent.com/63636498/82181485-3f57f480-9900-11ea-800f-830ce9b4f7ce.png)
   
   Type `y` or `yes` and hit `ENTER` to quit. 
   
   If you don't want to quit just hit `ENTER` and the game will continue.
   
### THANK YOU

