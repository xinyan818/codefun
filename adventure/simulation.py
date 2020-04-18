from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
from game import Game
import sys

def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""
	paths = []
	with open(source, 'r') as f:
		for path_text in f.readlines():
			path_params = [i.strip() for i in path_text.split('>')]
			paths.append(path_params)
	return paths


def create_rooms(paths):
	"""Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""
	rooms = {}
	for path in paths:
		try:
			if not rooms.get(path[0]):
				rooms[path[0]] = Room(path[0])
			if not rooms.get(path[2]):
				rooms[path[2]] = Room(path[2])
			rooms[path[0]].set_path(path[1], rooms[path[2]])
		except:
			continue
	if not rooms:
		print("No rooms exist! Exiting program...")
		exit()
	return rooms


def generate_items(source):
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""

	# TODO
	items = {}
	with open(source, 'r') as f:
		for item_text in f.readlines():
			if not item_text:
				continue
			item_value = [i.strip() for i in item_text.split('|')]
			items[item_value[0]] = Item(item_value[0], item_value[1], item_value[2], item_value[3])
	return items


def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""
	
	# TODO
	quests = []
	with open(source, 'r') as f:
		for quest_text in f.readlines():
			if not quest_text.strip():
				continue
			quest_value = [i.strip() for i in quest_text.split('|')]
			reward = items[quest_value[0]]
			room = rooms[quest_value[-1]]
			quest = Quest(reward, quest_value[1], quest_value[2], 
						  quest_value[3], quest_value[4], quest_value[5], 
						  quest_value[6], quest_value[7], room)
			room.set_quest(quest)
			quests.append(quest)
	return quests

if __name__ == "__main__":
	
# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.
	if len(sys.argv) < 4:
		print("Usage: python3 simulation.py <paths> <items> <quests>")
		exit()
	def path_exists(path):
		try:
			f = open(path)
			f.close()
		except Exception as e:
			print(e)
			return False
		else:
			return True

	if not (all(map(lambda path: path_exists(path), sys.argv[1:]))):
		print("Please specify a valid configuration file.")
		exit()
	
	paths = read_paths(sys.argv[1])
	rooms = create_rooms(paths)
	items = generate_items(sys.argv[2])
	quests = generate_quests(sys.argv[3], items, rooms)

# TODO: Receive commands from standard input and act appropriately.
	this_room = list(rooms.values())[0]
	player = Adventurer()
	game = Game(this_room, player, quests)
	game.look()
	while True:
		cmd = input(">>> ")
		game.execute_cmd(cmd)
