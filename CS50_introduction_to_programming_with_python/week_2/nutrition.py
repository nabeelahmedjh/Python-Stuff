
def main():
    while True:
        user_input = input("Item: ").lower()
        if (check_calories(user_input) != 0):
            print(f"Calories: {check_calories(user_input)}")
            break


def check_calories(user_input):
    fruits_calories = {"apple": 130,
                       "avocando": 50,
                       "banana": 110,
                       "cantaloupe": 50,
                       "grapefruit": 60,
                       "grapes": 90,
                       "honeydew melon": 90,
                       "kiwifruit": 90,
                       "lemon": 15,
                       "lime": 20,
                       "nectarine": 60,
                       "orange": 80,
                       "peach": 60,
                       "pineapple": 50,
                       "plums": 70,
                       "strawberries": 50,
                       "sweet cherries": 100,
                       "tangerine": 50,
                       "watermelon": 80
                       }
    if user_input not in fruits_calories:
        return 0

    return fruits_calories[user_input]


main()
