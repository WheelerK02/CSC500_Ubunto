import random


class Character:
    def __init__(self, name, health, primary, alternate, backup):
        # Setting up the starting attributes
        self.name = name
        self.health = health
        self.primary = primary
        self.alternate = alternate
        self.backup = backup

        # Nesting the dictionary right inside the object!
        self.character_build = {
            name: {
                'health': health,
                'wpns': {
                    'primary': primary,
                    'alternate': alternate,
                    'backup': backup
                }
            }
        }
        
    def primary_weapon(self, enemy):
        current_wpn =self.character_build[self.name]['wpns']['primary']
        
        
        
        if current_wpn == 'gun':
            print("self.name, shoots with his gun!")
            damage_amount = 10
            
        elif current_wpn == 'sword':
            print("self.name, slashes with his sword!")
            damage_amount = 5
        else:
            print("self.name, attacks with his backup weapon!")
            damage_amount = 2

    def attack(self, enemy):
        
        wpn = self.character_build[self.name]['wpns']['primary']
        damage_amount = 0
        if wpn == 'gun':
            
            damage_amount = 10
        elif wpn == 'sword':
            
            damage_amount = 5
        else:
            damage_amount = 2
            
        enemy.health = enemy.health - damage_amount
        
        print(F'{self.name} hits {enemy.name} for {damage_amount} damage! {enemy.name} has {enemy.health} health left.')
        
    def health_status(self):
        if self.health > 80:
            print(f"{self.name} is ready to fight! ⚡")
        elif self.health <= 80 and self.health > 60:
            print(f"{self.name} is on the ropes! 🥊")
        elif self.health <= 60 and self.health >= 40:
            print(f"Finish him! {self.name} is fading fast. 🔥")
        else:
            print(f"{self.name} retreats from the battle! 🏃")
            
def player_choice():
    player_fighter = None
    menu = ()
    choice = ''
    while choice != 'q':
        print('Player Choice')
        print('B - Choose Beast')
        print('H - Choose Hog')
        print('F - Choose Flash')
        print('I - Choose Ice  ')
        print('q - Quit')
        
        choice = input('Choose an option: ').strip().lower()
        
        if choice == 'b':
            print('You have chosen Beast!')
            return Beast
           
            
        elif choice == 'h':
            print('You have chosen Hog!')
            return Hog
           
            
        elif choice == 'f':
            print('You have chosen Flash!')
            return Flash
        
        elif choice == 'i':
            print('You have chosen Ice!')
            return Ice
            
        elif choice == 'q':
            print('Exiting the game...')
            break
        else:
            print('Invalid choice. Please choose again.')
            
    
            
            
# create beast character
Beast = Character("Beast", 65, 'gun', 'knife', 'grenade')
Hog = Character("Hog", 100, 'sword', 'shield', 'potion')
Flash = Character("Flash", 80, 'grenade', 'gun', 'potion')
Ice = Character("Ice", 72, 'knife', 'gun', 'shield')


player_fighter = player_choice()
opponents = [Beast, Hog, Flash, Ice]
opponents.remove(player_fighter)
Computer = random.choice(opponents)



while player_fighter.health >= 40 and Computer.health >= 40:
    player_fighter.attack(Computer)
    Computer.health_status()
    if Computer.health >= 40:
        Computer.attack(player_fighter)
    player_fighter.health_status()   
        




