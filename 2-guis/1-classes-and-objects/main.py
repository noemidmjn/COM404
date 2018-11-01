# the objects 
from bot import Bot

from superbot import SuperBot

from flyingbot import FlyingBot
  
beep = Bot("Beep", 3, 100, 80)
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()
beep.display_summary()

print("beep is", beep.get_age())
beep.get_energy()
beep.get_name()
beep.get_shield()

beep.decrement_energy(4)
beep.display_summary()

beep.decrement_shield(5)
beep.display_summary()

beep.increment_age(2)
beep.display_summary()

beep.increment_energy(8)
beep.display_summary()

beep.increment_shield(6)
beep.display_summary()

beep.set_name("Beep2")
beep.display_summary()


s_beep = SuperBot("Super Beep", 5, 60, 19, 2)

s_beep.get_super_power_level
s_beep.set_super_power_level(15)
s_beep.get_super_power_level

f_beep = FlyingBot("Flying Beep", 5, 60, 50, 6, 5)
f_beep.get_hover_distance
f_beep.set_hover_distance(5)
f_beep.get_hover_distance
