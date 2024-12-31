# i. import diablo2
# import diablo2
#
# print(diablo2.basic_energy)
# print(diablo2.sing())
#
# jain = diablo2.Amazon()
# print(jain.strength)
# print(jain.attack())
#
# eve = diablo2.Amazon()
# print(eve.vitality)
# eve.exercise()
# print(eve.vitality)

# 2. from diablo2 import *

# from diablo2 import *
#
# print(basic_energy)
# print(sing())
#
# lee = Amazon()
# print(lee.attack())
# lee.exercise()
# print(lee.strength)
# 3. from diablod import Amazon, sing

from diablo2 import Amazon, sing
print(sing())

kim = Amazon()
kim.exercise()
kim.exercise()
print(kim.strength)
