import random
from random import randint
import requests

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = random.randint(50,100)
        self.power = random.randint(5, 10)
        Pokemon.pokemons[pokemon_trainer] = self


    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = random.randint(1,5)
            if chance == 1:
                return 'Покемон-волшебни применил щит в сражении'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}'
        else:
            enemy.hp = 0
            return f'Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}'

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\n Здоровье твоего покемона: {self.hp}\n Атака твоего покемона: {self.power}"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    pass
class Fighter:
    def attack(self, enemy):
        super_power = random.randint(10,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'\nБоец приминил супер-атаку силой:{super_power}'
