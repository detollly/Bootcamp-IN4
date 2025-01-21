from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()

dave.set_conversation("Hello there!")
dave.talk()
dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input("\n> ")
dave.fight(fight_with)
print(dave.name)

