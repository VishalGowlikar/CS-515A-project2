import json
import sys


class adventure:
    @staticmethod
    def load_rooms(filepath):
        with open(filepath) as file:
            return json.load(file)

    @staticmethod
    def print_room_info(room):
        print("\n>  " + room['name'] + '\n')
        print(room['desc'] + '\n')
        if 'items' in room and room['items']:
            print('Items:', ', '.join(room['items']) + '\n')
        print('Exits:', ', '.join(room['exits']) + '\n')

    @staticmethod
    def move_to_next_room(data, current_room, direction):
        exits = data[current_room]['exits']
        if direction in exits:
            return exits[direction]
        else:
            print("There is no room in that direction.")
            return current_room

    @staticmethod
    def get_item(data, current_room, item, inventory):
        if item:
            if 'items' in data[current_room] and item in data[current_room]['items']:
                inventory.append(item)
                data[current_room]['items'].remove(item)
                print(f"You pick up the {item}.")
            else:
                print(f"There's no {item} anywhere.")
        else:
            print("Sorry, you need to 'get' something.")

    @staticmethod
    
    def drop_item(data, current_room, item, inventory):
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


        

    @staticmethod
    def show_inventory(inventory):
        if not inventory:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in inventory:
                print(f"  {item}")

    def help():
        print("You can run the following commands:")
        print("  go...")
        print("  get...")
        print("  look")
        print("  inventory")
        print("  quit")
        print("  help")
def main(file):
    data = adventure.load_rooms(file)
    current_room = 0
    inventory = []
    adventure.print_room_info(data[current_room])

    while True:
        try:
            action = input("What would you like to do? ").lower().strip()
        except EOFError:
            print("use 'quit' to exit.")
            continue
        if action == 'go':
            print("Sorry, you need to 'go' somewhere")

        elif action.startswith('go '):
            direction = action.split(' ', 1)[-1]  # Get the direction to move
            current_room = adventure.move_to_next_room(data, current_room, direction)

            # Print information about the new room or stay in the current room
            if current_room != -1:
                adventure.print_room_info(data[current_room])

        elif action == 'look':
            adventure.print_room_info(data[current_room])

        elif action.startswith('get '):
                
                item = action.split(' ', 1)[-1]
                adventure.get_item(data, current_room, item, inventory)

        elif action == 'inventory':
            adventure.show_inventory(inventory)

        elif action == 'drop':
            print("Specify an item to drop.")
        elif action.startswith('drop '):
            item = action.split(' ', 1)[-1]
            adventure.drop_item(data, current_room, item, inventory)

        elif action == 'quit':
            print("Goodbye!")
            break
        elif action == 'help':
            adventure.help()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    file = sys.argv[1]
    main(file)
