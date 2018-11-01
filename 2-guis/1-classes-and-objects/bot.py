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
