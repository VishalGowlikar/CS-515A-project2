import json
import sys

class adventure:
    def load_rooms(filepath):
        with open(filepath) as file:
            return json.load(file)

    def look(room):
        print(f"> {room['name']}\n\n{room['desc']}\n")
        if 'items' in room and room['items']:
            print('Items:', ', '.join(room['items'])+'\n')
        print('Exits:', ' '.join(room['exits'])+'\n' )

    def go(data, current_room, direction):
        exits = data[current_room]['exits']
        if direction in exits:
            print(f"You go {direction}.\n")
            return exits[direction]
        else:
            print(f"There's no way to go {direction}.")
            return current_room

    def get(data, current_room, item, inventory):
        if item:
            if 'items' in data[current_room] and item in data[current_room]['items']:
                inventory.append(item)
                data[current_room]['items'].remove(item)
                print(f"You pick up the {item}.")
            else:
                print(f"There's no {item} anywhere.")
        else:
            print("Sorry, you need to 'get' something.")

    def drop(data, current_room, item, inventory):
        if item:
            if 'items' in data[current_room] and item in inventory:
                inventory.remove(item)
                data[current_room]['items'].append(item)
                print(f"You drop the {item}.")
            elif item not in inventory:
                print(f"You're not carrying {item}.")
            else:
                print(f"There's no {item} to drop in this room.")
        else:
            print("Sorry, you need to 'drop' something.")

    def inventory(inventory):
        if not inventory:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in inventory:
                print(f"  {item}")
    def win_condition(data, current_room, inventory):
        last_room_index = len(data) - 1

        if current_room == last_room_index and 'win' in inventory:
            print("Congratulations! You win the game!")
            return True
        elif 'win' in inventory:
            print("Sorry, you can't use the 'win' command here. You lose!")
            return True
        return False

    def help():
        print("You can run the following commands:")
        print("  go ...")
        print("  get ...")
        print("  drop ...")
        print("  look")
        print("  inventory")
        print("  quit")
        print("  help")

def main(file):
    data = adventure.load_rooms(file)
    current_room = 0
    inventory = []
    adventure.look(data[current_room])

    while True:
        try:
            action = input("What would you like to do? ").lower().strip()
        except EOFError:
            print("use 'quit' to exit.")
            continue

        if action == 'go':
            print("Sorry, you need to 'go' somewhere.")
        elif action.startswith('go '):
            direction = action.split(' ', 1)[-1]  # Get the direction to move
            temp = current_room
            current_room = adventure.go(data, current_room, direction)
            if temp == current_room:
                pass
            else:
                adventure.look(data[current_room])

        elif action == 'look':
            adventure.look(data[current_room])

        elif action.startswith('get '):
            if action[1]:
                item = action.split(' ', 1)[-1]
                adventure.get(data, current_room, item, inventory)
            else:
                print("You need to 'get' something.")
        elif action == 'get':
            print("Sorry, you need to 'get' something.")

        elif action == 'inventory':
            adventure.inventory(inventory)

        elif action == 'drop':
            print("Sorry, you need to 'drop' something.")
        elif action.startswith('drop '):
            item = action.split(' ', 1)[-1]
            adventure.drop(data, current_room, item, inventory)

        elif action == 'quit':
            print("Goodbye!")
            break
        elif action == 'help':
            adventure.help()

        elif action == 'win':
            if current_room == len(data) - 1:  # Check if the 'win' command is in the last room
                inventory.append('win')  # Add 'win' to inventory to trigger the win_condition()
                if adventure.win_condition(data, current_room, inventory):
                    break
            else:
                print("Sorry you had lose the game. CAUSE: you have not enter the black room")
                break
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    file = sys.argv[1]
    main(file)
