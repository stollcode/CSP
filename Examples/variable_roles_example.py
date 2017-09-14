'''
* Variable Roles Examples
'''

"""
  FIXED VARIABLE

  Move the sprite five pixels down and to the left for each loop iteration

"""
print("*** FIXED ***")
MOVE_INCREMENT = 4
x = 100
y = 100

for i in range(10):
    y = y + MOVE_INCREMENT
    x = x - MOVE_INCREMENT
    print("Sprite at position x:", x, "y:", y)

"""







  MOST RECENT VARIABLE

  Move x and y store the most recent value at each loop iteration.

"""
print("*** MOST RECENT ***")
x = 0
y = 0

for i in range(10):
    y = y + 2
    x = x + i
    print("Most recent position x:", x, "y:", y)

"""
  ACCUMULATOR VARIABLE
  Sum the number of times the loop iterates.
"""
print("*** ACCUMULATOR ***")
accumulator = 0
for i in range(1000):
    accumulator = accumulator + i
print("Total Value:", accumulator)

"""
  AGGREGATOR VARIABLE
  armorList.
"""
print("*** AGGREGATOR (List) ***")
armorList = ['Cuirass', 'Leggings', 'Boots', 'Gauntlets', 'Shield']
print("List before adding ring:", armorList)
armorList.append("Ring of Hircine")
print("List after adding ring:", armorList)

"""
  STEPPER  VARIABLE
  printing armorList using the stepper variable: "listPosition".
"""
print("*** Stepper ***")
armorList = ['Cuirass', 'Leggings', 'Boots', 'Gauntlets', 'Shield']
listPosition = 0

while listPosition < len(armorList):
    print("armorList Item:", armorList[listPosition])
    listPosition = listPosition + 1

"""
  WALKER VARIABLE
  printing armorList using the walker variable: "item".
"""
print("*** Walker ***")
armorList = ['Cuirass', 'Leggings', 'Boots', 'Gauntlets', 'Shield']

for item in armorList:
    print("armorList Item:", item)

"""
  BEST-SO-FAR VARIABLE
  printing armorList using the walker variable: "highScore".
"""
highScore = 556
print("*** High Score ***")
print("High Score:", highScore)

"""
  ONE-WAY-FLAG VARIABLE
  onEdge flag.
"""
print("*** One-Way-Flag ***")
# When user starts game
onEdge = False
x = 10
print("onEdge:", onEdge)

while onEdge != True:
    x = x + 1
    print(x)
    if x >= 600:
        onEdge = True

