class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Syringe(Weapon):
	def __init__(self):
		super().__init__(name="Syringe", description="Empty, but still sharp", value=2, damage=3)

class Cash(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Cash", description="A pile of {} bills".format(str(self.amt)), value=self.amt)

