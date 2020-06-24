# import sys


class CoffeeMachine:
    # Machine Initial Quantity
    machine_water = 400
    machine_milk = 540
    machine_coffee = 120
    machine_cups = 9
    machine_money = 550

    # 1 espresso
    espresso_water = 250
    espresso_coffee = 16
    espresso_cost = 4

    # 2 latte
    latte_water = 350
    latte_milk = 75
    latte_coffee = 20
    latte_cost = 7

    # 3 cappuccino
    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_coffee = 12
    cappuccino_cost = 6

    def __init__(self):
        self.again = True

    def actions(self):
        while self.again:
            action = input("\nWrite action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                self.again = False
            else:
                print("wrong input")

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if choice == "1":
            if self.machine_water <= self.espresso_water:
                print("Sorry, not enough water!")
            elif self.machine_coffee <= self.espresso_coffee:
                print("Sorry, not enough beans!")
            elif self.machine_cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.machine_water -= self.espresso_water
                self.machine_coffee -= self.espresso_coffee
                self.machine_money += self.espresso_cost
                self.machine_cups -= 1
                print("I have enough resources, making you a coffee!")

        elif choice == "2":
            if self.machine_water <= self.latte_water:
                print("Sorry, not enough water!")
            elif self.machine_coffee <= self.latte_coffee:
                print("Sorry, not enough beans!")
            elif self.machine_milk <= self.latte_milk:
                print("Sorry, not enough milk!")
            elif self.machine_cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.machine_water -= self.latte_water
                self.machine_coffee -= self.latte_coffee
                self.machine_money += self.latte_cost
                self.machine_cups -= 1
                self.machine_milk -= self.latte_milk

                print("I have enough resources, making you a coffee!")

        elif choice == "3":
            initial_water = self.machine_water
            if initial_water <= self.cappuccino_water:
                print("Sorry, not enough water!")
            elif self.machine_coffee <= self.cappuccino_coffee:
                print("Sorry, not enough beans!")
            elif self.machine_milk <= self.cappuccino_milk:
                print("Sorry, not enough milk!")
            elif self.machine_cups == 0:
                print("Sorry, not enough cups!")
            else:

                self.machine_water -= self.cappuccino_water
                self.machine_coffee -= self.cappuccino_coffee
                self.machine_money += self.cappuccino_cost
                self.machine_cups -= 1
                self.machine_milk -= self.cappuccino_milk

                print("I have enough resources, making you a coffee!")

        elif choice == 'back':
            self.actions()

        else:
            print('Wrong Choice')

    def fill(self):
        self.machine_water = self.machine_water + int(input("Write how many ml of water do you want to add:"))
        self.machine_milk = self.machine_milk + int(input("Write how many ml of milk do you want to add:"))
        self.machine_coffee = self.machine_coffee + int(
            input("Write how many grams of coffee beans do you want to add:"))
        self.machine_cups = self.machine_cups + int(
            input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you $%d\n" % self.machine_money)
        self.machine_money = 0

    def remaining(self):
        self.print_remaining()

    def print_remaining(self):
        print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money'''.format(self.machine_water, self.machine_milk, self.machine_coffee, self.machine_cups,
                       self.machine_money))


coffee_machine = CoffeeMachine()
coffee_machine.actions()
