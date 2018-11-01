from bot import Bot

from superbot import SuperBot

class FlyingBot(SuperBot):
  def __init__(self, name, age, energy, shield, super_power_level, hover):
    super().__init__(name, age, energy, shield, super_power_level)
    self.hover = hover

  def get_hover_distance(self):
    return hover

  def set_hover_distance(self, distance):
    self.hover = distance
