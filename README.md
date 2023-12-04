# CS515-Project1  Text-Based Adventure Game

## Author Information
Gowlikar Vishal
Vgowlika@stevens.edu

## Repository
[Github Repository](https://github.com/VishalGowlikar/CS-515A-project2)

## Time spent on the project
Estimated time spent: 27 hours


## How to execute the program
1. Install python3
2. Clone the git repository or download the map file, adventure.py file to a folder
3. Navigate to the folder and run the command `adventure.py [map filename]`

## Overview
These is the text-based game which is played in the form of texting the commands. where the player enter in the different world which is enriched with the immersive things, clean-environment at the fullest of adventure,mysteries and awards.


## executing the program in following steps using the verbs:
Several verbs which can be used as commands in the game are:

1. **go**: The go verb basically tries to go in the given direction. You can use the command by typing `go [direction]` with direction as a valid exit.

2. **look**:  Now,The look command shows once again the room that a person is in. You can use the command by just typing `look` in the command line.

3. **get**: The get verb shows you or the player to pick up the items that are in that room. When a player says `get [ITEM]` example command: ( GET ROSE ), if that item is in the room, the player will pick it up, the item will no longer be in the room but rather it will be in the player’s inventory, we can see/access it by typing a command inventory in command line. `[WORKING OF THE INVENTORY IS IN THE FOLLOWING]` 

4. **drop**:  It is the just opposite of the get like the get verb lets a player drop the items that are in his inventory to the room he is in. When a player says `drop [ITEM]`, if that item is in the inventory, the player will drop it, the item will no longer be in the inventory. 

5. **inventory**: The inventory verb shows the player the list of the items they are carrying. by using the command:`[inventory]`

6. **help**: The help verb gives the player the list of all the valid verbs.

7. **quit**: The 'quit' verb ends the game and exits the program.

8. **win**: the 'win' verb shows that you have won or lose and exist the program if you lose or win.



## How the code was tested
I have tested the code manually by running on my machine it against different test cases and with multiple map files. like ambig.map, loop.map, dir.map. I have also tested it using the provided spec and using diff to compare the outputs.

## Bugs or issues
No bugs or issues

## Difficult issue or bug and its resolution
I had an issue with the arbitary spaces, arbitary line spaces and also the game direction in the inputs and I have compared the decription provided in the project for multiple times. 

## Extensions implemented:
1. **Help Verb**: I have implemented a dynamic help verb that lists out all the valid verbs for the game. I have listed out all the methods in the player class by using harcore function help by printing all verbs used. The help ver can be accessed by just typing `help`.
   In my example, the command `help` can be used anywhere to get the list of valid verbs.
   
2. **Winning and Losing Conditions**: I have a winning condition in the game that a player wins if the player uses the verb `win` when he is in the last room of the map with having the inventory list with the item in my red room consists rose using the loop.map. He loses the game in case he uses the command when he is in any other room without the item in the inventory. 
Example: Consider we have a map with 5 rooms. If the player is in the 5th room i.e. the last room and have a item from the blue room in his inventory he gives the command `win`, he'd win whereas, if the player is in the 4th room and he gives the command `win`, he'd lose. 
In my example map, the Goalroom(the last is where the player can give a command `win` to win the game.
Step 1: go east
step 2: get rose
step 3: go north
step 4: go west
step 5: go south
step 6: win

3. **Drop Verb**: I have applied a drop verb to allow the player to drop an item in a room. The item will be removed from the inventory and be placed in the room the player where he picked it. To use the verb, the player can type `drop [item]` with a valid item existing in the inventory.
In my example, the player can go to any room where there are any items to pick them up and then he can use the `drop` verb to drop any items he has in his inventory only in the room where he picked it.
