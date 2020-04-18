class Game:

	def __init__(self, room, player, quests=[]):
		self.room = room
		self.player = player
		self.quests = quests

	def execute_cmd(self, cmd):

		cmd_ = cmd.strip().upper()
		quest = self.room.get_quest()
		if quest and not quest.is_complete() and (quest.get_action() == cmd_):
			quest.attempt(self.player)
		else:
			cmd_map = {
				"HELP": self.help,
				"QUIT": self.quit,
				"LOOK": self.look,
				"L": self.look,
				"QUESTS": self.get_quests,
				"CHECK": self.check,
				"INV": self.inv,
				"NORTH": self.north, 
				"N": self.north, 
				"SOUTH": self.south,
				"S": self.south,
				"EAST": self.east,
				"E": self.east,
				"WEST": self.west,
				"W": self.west,
			}
			if cmd_map.get(cmd_):
				task = cmd_map[cmd_]
				task()
			else:
				print()
				print("You can't do that.")

	def quit(self):
		print("Bye!")
		exit()
	
	def look(self):
		self.room.draw()
		msg = "You are standing at the %s." % self.room.get_name()
		print(msg)
		print(self.room.get_short_desc())
		print()

	def help(self):
		text = """
HELP - Shows some available commands.
LOOK or L - Lets you see the map/room again.
QUESTS - Lists all your active and completed quests.
INV - Lists all the items in your inventory.
CHECK - Lets you see an item (or yourself) in more detail.
NORTH or N - Moves you to the north.
SOUTH or S - Moves you to the south.
EAST or E - Moves you to the east.
WEST or W - Moves you to the west.
QUIT - Ends the adventure."""
		print(text)

	def get_quests(self):
		for idx, quest in enumerate(self.quests):
			num = '#%s:' % (idx if idx > 9 else '0%s' % idx)
			reward = quest.reward.get_name() if len(quest.reward.get_name()) >= 21 \
											 else quest.reward.get_name() + " "*(21 - len(quest.reward.get_name()))
			desc = '- %s' % quest.get_info()
			completed = '[COMPLETED]' if quest.is_complete() else ''
			print(' '.join([num, reward, desc, completed]))
		if len([quest for quest in self.quests if not quest.is_complete()]) == 0:
			print()
			print("=== All quests complete! Congratulations! ===")
			exit()
	
	def inv(self):
		print("You are carrying:")
		inv = self.player.get_inv()
		if inv:
			for item in inv: 
				print("- A %s" % item.get_name())
		else:
			print("Nothing.")

	def check(self):
		check_item = input("Check what? ").strip().upper()
		if check_item == "ME":
			self.player.check_self()
		else:
			for item in self.player.get_inv():
				if item.get_name().strip().upper == check_item or item.get_short() == check_item:
					item.get_info()
					return
			print("\nYou don't have that!\n")

	def north(self):
		self.move("north")		
	
	def south(self):
		self.move("south")		

	def east(self):
		self.move("east")		
	
	def west(self):
		self.move("west")

	def move(self, dir):
		move_room = self.room.move(dir.upper())
		if move_room:
			self.room = move_room
			print("You move to the %s, arriving at the %s." % (dir, self.room.get_name()))
			self.look()
		else:
			print("You can't go that way.")
			