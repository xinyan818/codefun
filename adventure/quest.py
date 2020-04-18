class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		"""TODO: Initialises a quest."""
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.set_req_value(req)
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.complate = False

	def set_req_value(self, req_text):
		values = req_text.split(',')
		self.req_skill = 0
		self.req_will = 0
		for v in values:
			if "SKILL" in v.upper():
				try:
					skill_value = int(v.strip("").strip("skill").strip("SKILL"))
				except Exception as e:
					print(v)
					print(e)
					skill_value = 0
				self.req_skill = skill_value
			elif "WILL" in v.upper():
				try:
					will_value = int(v.strip("").strip("will").strip("WILL"))
				except Exception as e:
					print(v)
					print(e)
					will_value = 0
				self.req_will = will_value
				
	def get_info(self):
		"""TODO: Returns the quest's description."""
		return self.desc

	def is_complete(self):
		"""TODO: Returns whether or not the quest is complete."""
		return self.complate

	def get_action(self):
		"""TODO: Returns a command that the user can input to attempt the quest."""
		return self.action.upper()

	def get_room_desc(self):
		"""TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		return self.after if self.complate else self.before 

	def attempt(self, player):
		"""TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""
		if player.get_skill() >= self.req_skill and player.get_will() >= self.req_will:
			self.complate = True
			if self.reward:
				player.take(self.reward)
			print(self.pass_msg)
			print()
		else:
			print(self.fail_msg)
			print()

		
