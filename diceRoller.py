import random

# Dice art dictionary
dice_art = {
    1: ("┌────────────┐",
        "│            │",
        "│     ●      │",
        "│            │",
        "└────────────┘"),

    2: ("┌────────────┐",
        "│  ●         │",
        "│            │",
        "│         ●  │",
        "└────────────┘"),

    3: ("┌────────────┐",
        "│  ●         │",
        "│     ●      │",
        "│         ●  │",
        "└────────────┘"),

    4: ("┌────────────┐",
        "│  ●      ●  │",
        "│            │",
        "│  ●      ●  │",
        "└────────────┘"),

    5: ("┌────────────┐",
        "│  ●      ●  │",
        "│     ●      │",
        "│  ●      ●  │",
        "└────────────┘"),

    6: ("┌────────────┐",
        "│  ●      ●  │",
        "│  ●      ●  │",
        "│  ●      ●  │",
        "└────────────┘")
}

# Ask how many dice
num_of_dice = int(input("How many dice do you want to roll?: "))

# Roll dice and store results
dice = [random.randint(1, 6) for _ in range(num_of_dice)]

# Print dice side by side
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end=" ")
    print()

# Calculate total
total = sum(dice)
print(f"\nThe total is: {total}")
