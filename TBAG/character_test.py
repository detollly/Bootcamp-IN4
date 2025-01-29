from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()

dave.set_conversation("Hello there!")
dave.talk()

dave.set_weakness("cheese")
dave.add_item("cheese")  # Adding item to enemy inventory

print("What will you fight with?")
fight_with = input("\n> ")

while not fight_with:  # Ensure input isn't empty
    print("You must choose something to fight with.")
    fight_with = input("\n> ")

dave.fight(fight_with)

print(f"Enemy name: {dave.name}")
