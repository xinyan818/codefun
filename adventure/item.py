class Item:
	def __init__(self, name, short, skill_bonus, will_bonus):
		"""TODO: Initialises an item."""
		self.name = name
		self.short = short
		self.skill_bonus = int(skill_bonus)
		self.will_bonus = int(will_bonus)

	def get_name(self):
		"""TODO: Returns an item's name."""
		return self.name

	def get_short(self):
		"""TODO: Returns an item's short name."""
		return self.short

	def get_info(self):
		"""TODO: Prints information about the item."""
		print("\n%s\n%s\n%s" 
			% (self.name, 
			   "Grants a bonus of %s to SKILL." % (self.skill_bonus), 
			   "Grants a bonus of %s to WILL.\n" % (self.will_bonus)))

	def get_skill(self):
		"""TODO: Returns the item's skill bonus."""
		return self.skill_bonus

	def get_will(self):
		"""TODO: Returns the item's will bonus."""
		return self.will_bonus
		
