class Bot:
  def __init__(self, name, age, energy, shield):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield = shield
  
  def display_name(self):
    print("{} is the name of the bot".format(self.name))

  def display_age(self):
    print("{} is the age of the bot".format(self.age))
  
  def display_energy(self):
    print("{} is the energy level of the bot".format(self.energy))

  def display_shield(self):
    print("{} is the energy level of the bot".format(self.energy))

  def display_summary(self):
    print("{} is {} years old and weights {}kg".format(self.name, self.age, self.energy, self.shield))

  def get_age(self):
    return self.age

  def get_energy(self):
    return self.energy

  def get_name(self):
    return self.name

  def get_shield(self):
    return self.shield

  def decrement_energy(self, amount):
    self.energy = self.energy - amount

  def decrement_shield(self, amount):
    self.shield = self.shield - amount

  def increment_age(self, amount):
    self.age = self.age + amount

  def increment_energy(self, amount):
    self.energy = self.energy + amount

  def increment_shield(self, amount):
    self.shield = self.shield + amount

  def set_name(self, name):
    self.name = name
