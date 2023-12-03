import json
import sys
import re



class Adventure:
    def look(self,desc,exits):
        # print("A white room', 'desc': 'You are in a simple room with white walls.', 'exits': {'north': 1, 'east': 3}}")
        self.desc = desc
        self.exits = exits

        i1 = Adventure("'desc': 'You are in a simple room with white walls.'","'exits': {'north': 1, 'east': 3} ")

        print(i1.desc)
        print(i1.exits)

    # Load the data from the JSON file
    def load_map(filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def display_room_info(room):
        print(f"> {room['name']}\n")
        print(room['desc'])
        print(f"\nExits: {' '.join(room['exits'])}\n")

    def main(file):
        # map = look(file)
        # print(map)
        while(True):
            print("WELCOME TO MY GAME")
            
            choice = input("WHAT WOULD YOU LIKE TO DO? ")
            if choice == "go":
                print("this is the normal ")

                
                
            elif choice == "quit":
                print("Goodbye")
                break


if __name__ == "__main__":
    file = sys.argv[1]
    Adventure.main(file)
