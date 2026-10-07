import random

dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for x in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for x in range(num_of_dice):
#    for line in dice_art.get(dice[x]):
#        print(line)

for line in range(5):
    for x in dice:
        print(dice_art.get(x)[line], end="")
    print()

for x in dice:
    total += x
print(f"total: {total}")