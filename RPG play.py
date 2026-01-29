import random
class Character:
    def __init__(self, race):
        self.race = race
        self.level = 1
        self.exp = 0
        self.exp_to_next = 100
        self.stat_points = 0

        # Генерация характеристик в зависимости от расы
        if race == "Человек":
            self.hp = random.randint(80, 100)
            self.max_hp = self.hp
            self.attack = random.randint(10, 15)
            self.defense = random.randint(8, 12)
            self.agility = random.randint(8, 12)
            self.height = random.randint(165, 185)
            self.weight = random.randint(65, 85)
        elif race == "Эльф":
            self.hp = random.randint(70, 90)
            self.max_hp = self.hp
            self.attack = random.randint(8, 13)
            self.defense = random.randint(6, 10)
            self.agility = random.randint(12, 18)
            self.height = random.randint(175, 195)
            self.weight = random.randint(55, 75)
        else:  # Дворф
            self.hp = random.randint(90, 120)
            self.max_hp = self.hp
            self.attack = random.randint(12, 18)
            self.defense = random.randint(10, 15)
            self.agility = random.randint(5, 9)
            self.height = random.randint(140, 160)
            self.weight = random.randint(70, 90)

        # Экипировка
        self.equipped_weapon = None
        self.equipped_armor = None

        # Инвентарь
        self.inventory = {
            "Зелье здоровья": 3,
            "Монеты": 50
        }

    def show_stats(self):
        """Показать характеристики персонажа"""
        print(f"\n=== ХАРАКТЕРИСТИКИ ПЕРСОНАЖА ===")
        print(f"Раса: {self.race}")
        print(f"Уровень: {self.level} (Опыт: {self.exp}/{self.exp_to_next})")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Атака: {self.attack}")
        print(f"Защита: {self.defense}")
        print(f"Ловкость: {self.agility}")
        print(f"Рост: {self.height} см")
        print(f"Вес: {self.weight} кг")
        print(f"Очки прокачки: {self.stat_points}")

        if self.equipped_weapon:
            print(f"Оружие: {self.equipped_weapon['name']} (+{self.equipped_weapon['attack']} к атаке)")
        if self.equipped_armor:
            print(f"Броня: {self.equipped_armor['name']} (+{self.equipped_armor['defense']} к защите)")

    def level_up(self):
        """Повышение уровня"""
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = int(self.exp_to_next * 1.5)
        self.stat_points += 3
        self.max_hp += 10
        self.hp = self.max_hp

        print(f"\n=== УРОВЕНЬ ПОВЫШЕН! ===")
        print(f"Новый уровень: {self.level}")
        print(f"Максимальное HP увеличено до {self.max_hp}")
        print(f"Получено 3 очка прокачки")

    def add_exp(self, amount):
        """Добавление опыта"""
        self.exp += amount
        print(f"Получено {amount} опыта!")

        while self.exp >= self.exp_to_next:
            self.level_up()

    def use_stat_point(self, stat):
        """Использовать очко прокачки"""
        if self.stat_points <= 0:
            print("Нет очков прокачки!")
            return False

        if stat == "hp":
            self.max_hp += 5
            self.hp += 5
        elif stat == "attack":
            self.attack += 1
        elif stat == "defense":
            self.defense += 1
        elif stat == "agility":
            self.agility += 1

        self.stat_points -= 1
        print(f"Характеристика {stat} улучшена!")
        return True


class Enemy:
    def __init__(self, floor):
        enemy_types = ["Гоблин", "Скелет", "Орк", "Тролль"]
        self.name = random.choice(enemy_types)
        self.level = max(1, floor - 1)  # Враги немного слабее игрока
        self.max_hp = random.randint(15, 25) + floor * 3
        self.hp = self.max_hp
        self.attack = random.randint(4, 8) + floor
        self.defense = random.randint(2, 5) + floor
        self.agility = random.randint(3, 10)
        self.height = random.randint(150, 220)
        self.weight = random.randint(60, 120)
        self.exp_reward = random.randint(20, 30) + floor * 3
        self.gold_reward = random.randint(5, 10) + floor * 2

    def show_stats(self):
        print(f"\n=== ХАРАКТЕРИСТИКИ ВРАГА ===")
        print(f"Имя: {self.name}")
        print(f"Уровень: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Атака: {self.attack}")
        print(f"Защита: {self.defense}")
        print(f"Ловкость: {self.agility}")
        print(f"Рост: {self.height} см")
        print(f"Вес: {self.weight} кг")


class Game:
    def __init__(self):
        self.player = None
        self.floor = 1
        self.rooms_cleared = 0
        self.rooms_on_current_floor = 0
        self.MAX_FLOORS = 3  # Максимальное количество этажей для победы
        self.ROOMS_PER_FLOOR = 3  # Количество комнат на этаж

    def create_character(self):
        """Создание персонажа"""
        print("\n" + "=" * 40)
        print("=== СОЗДАНИЕ ПЕРСОНАЖА ===")
        print("=" * 40)
        print("Выберите расу:")
        print("1 - Человек (сбалансированный)")
        print("2 - Эльф (ловкий)")
        print("3 - Дворф (сильный и выносливый)")

        while True:
            choice = input("\nВаш выбор (1-3): ")
            if choice == "1":
                race = "Человек"
                break
            elif choice == "2":
                race = "Эльф"
                break
            elif choice == "3":
                race = "Дворф"
                break

        self.player = Character(race)
        print(f"\n=== ВАШ ПЕРСОНАЖ СОЗДАН! ===")
        print(f"Раса: {race}")
        self.player.show_stats()
        input("\nНажмите Enter, чтобы начать исследовать подземелье...")
        print("\n" + "=" * 40)
        print(f"Вы входите в подземелье (Этаж {self.floor}/3)...")
        print("=" * 40)

    def show_inventory(self):
        """Показать инвентарь"""
        print("\n=== ИНВЕНТАРЬ ===")

        if not self.player.inventory:
            print("Инвентарь пуст!")
            return

        for i, (item, quantity) in enumerate(self.player.inventory.items(), 1):
            print(f"{i}. {item}: {quantity}")

        print("\nЭкипировка:")
        if self.player.equipped_weapon:
            print(f"Оружие: {self.player.equipped_weapon['name']}")
        else:
            print("Оружие: Нет")

        if self.player.equipped_armor:
            print(f"Броня: {self.player.equipped_armor['name']}")
        else:
            print("Броня: Нет")

        print("\n1. Использовать зелье здоровья")
        print("2. Экипировать предмет")
        print("3. Выбросить предмет")
        print("4. Продолжить исследование")

        while True:
            choice = input("\nВыберите действие: ")

            if choice == "1" and "Зелье здоровья" in self.player.inventory:
                if self.player.hp == self.player.max_hp:
                    print("У вас и так полное здоровье!")
                else:
                    heal = 30
                    self.player.hp = min(self.player.max_hp, self.player.hp + heal)
                    self.player.inventory["Зелье здоровья"] -= 1
                    if self.player.inventory["Зелье здоровья"] <= 0:
                        del self.player.inventory["Зелье здоровья"]
                    print(f"Вы восстановили {heal} HP!")
                break

            elif choice == "2":
                self.equip_item_menu()
                break

            elif choice == "3":
                item_name = input("Введите название предмета для удаления: ")
                if item_name in self.player.inventory:
                    if item_name == "Монеты":
                        print("Нельзя выбрасывать монеты!")
                    else:
                        del self.player.inventory[item_name]
                        print(f"Предмет {item_name} удален!")
                break

            elif choice == "4":
                break

            else:
                print("Неверный выбор!")

    def equip_item_menu(self):
        """Меню экипировки предметов"""
        print("\n=== ЭКИПИРОВКА ===")

        weapons = [k for k in self.player.inventory.keys() if "меч" in k.lower()]
        armors = [k for k in self.player.inventory.keys() if "броня" in k.lower()]

        if weapons:
            print("\nДоступное оружие:")
            for i, weapon in enumerate(weapons, 1):
                print(f"{i}. {weapon}")

            choice = input("\nВыберите оружие для экипировки (0 - снять): ")
            if choice == "0":
                self.player.equipped_weapon = None
                print("Оружие снято!")
            elif choice.isdigit() and 1 <= int(choice) <= len(weapons):
                weapon_name = weapons[int(choice) - 1]
                if "Простой меч" in weapon_name:
                    self.player.equipped_weapon = {"name": weapon_name, "attack": 2}
                else:
                    self.player.equipped_weapon = {"name": weapon_name, "attack": 1}
                print(f"Экипировано: {weapon_name}")

        if armors:
            print("\nДоступная броня:")
            for i, armor in enumerate(armors, 1):
                print(f"{i}. {armor}")

            choice = input("\nВыберите броню для экипировки (0 - снять): ")
            if choice == "0":
                self.player.equipped_armor = None
                print("Броня снята!")
            elif choice.isdigit() and 1 <= int(choice) <= len(armors):
                armor_name = armors[int(choice) - 1]
                if "Кожаная броня" in armor_name:
                    self.player.equipped_armor = {"name": armor_name, "defense": 2}
                else:
                    self.player.equipped_armor = {"name": armor_name, "defense": 1}
                print(f"Экипировано: {armor_name}")

        if not weapons and not armors:
            print("Нет предметов для экипировки!")

    def battle(self, enemy):
        """Боевая система"""
        print(f"\n{'=' * 50}")
        print(f"БОЙ С {enemy.name.upper()}")
        print(f"{'=' * 50}")
        print(f"Вы встретили {enemy.name}!")
        enemy.show_stats()

        while enemy.hp > 0 and self.player.hp > 0:
            print(f"\nВаше HP: {self.player.hp}/{self.player.max_hp}")
            print(f"HP {enemy.name}: {enemy.hp}/{enemy.max_hp}")

            print("\nВаши действия:")
            print("1. Атаковать")
            print("2. Использовать предмет")
            print("3. Попытаться уклониться")

            try:
                choice = int(input("Выберите действие: "))

                if choice == 1:
                    # Игрок атакует
                    base_damage = self.player.attack
                    if self.player.equipped_weapon:
                        base_damage += self.player.equipped_weapon['attack']

                    # Формула урона
                    player_damage = max(1, base_damage - enemy.defense // 3)

                    # Шанс критического удара
                    if random.randint(1, 100) <= self.player.agility:
                        player_damage *= 2
                        print("Критический удар!")

                    old_enemy_hp = enemy.hp
                    enemy.hp -= player_damage
                    if enemy.hp < 0:
                        enemy.hp = 0

                    print(f"Вы нанесли {player_damage} урона {enemy.name}!")
                    print(f"{enemy.name}: {old_enemy_hp} HP -> {enemy.hp} HP")

                elif choice == 2:
                    self.show_inventory()
                    if self.player.hp <= 0:
                        break
                    continue

                elif choice == 3:
                    # Попытка уклониться
                    dodge_chance = min(80, self.player.agility * 2)
                    if random.randint(1, 100) <= dodge_chance:
                        print("Вы приготовились уклониться от следующей атаки!")
                    else:
                        print("Не удалось сконцентрироваться для уклонения!")

                else:
                    print("Вы пропускаете ход!")

                # Проверка, жив ли враг
                if enemy.hp <= 0:
                    break

                # Атака врага (если выбор не был уклонением или уклонение не удалось)
                if choice != 3 or random.randint(1, 100) > min(80, self.player.agility * 2):
                    enemy_damage = max(1, enemy.attack - self.player.defense // 2)
                    if self.player.equipped_armor:
                        enemy_damage -= self.player.equipped_armor['defense']
                        enemy_damage = max(1, enemy_damage)

                    old_player_hp = self.player.hp
                    self.player.hp -= enemy_damage
                    if self.player.hp < 0:
                        self.player.hp = 0

                    print(f"{enemy.name} нанес вам {enemy_damage} урона!")
                    print(f"Ваше HP: {old_player_hp} -> {self.player.hp}/{self.player.max_hp}")

            except ValueError:
                print("Пожалуйста, введите число")

        # Результат боя
        if enemy.hp <= 0:
            print(f"\nПОБЕДА! Вы победили {enemy.name}!")

            # Награда
            print(f"Получено опыта: {enemy.exp_reward}")
            print(f"Получено золота: {enemy.gold_reward}")

            self.player.inventory["Монеты"] = self.player.inventory.get("Монеты", 0) + enemy.gold_reward
            self.player.add_exp(enemy.exp_reward)

            # Шанс получить предмет
            if random.randint(1, 100) <= 40:
                items = ["Зелье здоровья", "Простой меч", "Кожаная броня"]
                item = random.choice(items)

                self.player.inventory[item] = self.player.inventory.get(item, 0) + 1

                if item == "Простой меч":
                    print(f"Найден предмет: {item} (Атака +2)")
                elif item == "Кожаная броня":
                    print(f"Найден предмет: {item} (Защита +2)")
                else:
                    print(f"Найден предмет: {item}")

            return True
        else:
            print(f"\nПОРАЖЕНИЕ! Вас победил {enemy.name}!")
            print(f"Характеристики победившего врага:")
            enemy.show_stats()
            return False

    def rest_room(self):
        """Комната отдыха"""
        print("\n=== КОМНАТА ОТДЫХА ===")
        print("Вы находите безопасное место для отдыха.")

        # Восстановление HP
        heal = int(self.player.max_hp * 0.5)
        self.player.hp = min(self.player.max_hp, self.player.hp + heal)
        print(f"Вы отдохнули и восстановили {heal} HP!")

        if self.player.stat_points > 0:
            print(f"\nУ вас есть {self.player.stat_points} очков прокачки.")
            upgrade = input("Хотите улучшить характеристики? (да/нет): ").lower()

            if upgrade == "да":
                while self.player.stat_points > 0:
                    print(f"\nОсталось очков: {self.player.stat_points}")
                    print("1. HP (+5)")
                    print("2. Атака (+1)")
                    print("3. Защита (+1)")
                    print("4. Ловкость (+1)")
                    print("5. Выйти")

                    choice = input("Выберите характеристику: ")

                    if choice == "5":
                        break

                    stats = {"1": "hp", "2": "attack", "3": "defense", "4": "agility"}
                    if choice in stats:
                        self.player.use_stat_point(stats[choice])
                    else:
                        print("Неверный выбор!")

        print("\n1. Продолжить исследование")
        print("2. Открыть инвентарь")

        while True:
            choice = input("\nВыберите действие: ")
            if choice == "1":
                break
            elif choice == "2":
                self.show_inventory()
                break
            else:
                print("Неверный выбор!")

    def treasure_room(self):
        """Комната с сокровищами"""
        print("\n=== КОМНАТА С СОКРОВИЩАМИ ===")

        # Виды наград
        rewards = [
            ("Зелье здоровья", random.randint(2, 4)),
            ("Монеты", random.randint(15, 40)),
            ("Простой меч", 1),
            ("Кожаная броня", 1)
        ]

        reward = random.choice(rewards)
        item, quantity = reward

        self.player.inventory[item] = self.player.inventory.get(item, 0) + quantity

        if item == "Простой меч":
            print(f"Вы нашли {item}! (Атака +2)")
        elif item == "Кожаная броня":
            print(f"Вы нашли {item}! (Защита +2)")
        else:
            print(f"Вы нашли {quantity} {item}!")

        print("\n1. Продолжить исследование")
        print("2. Открыть инвентарь")

        while True:
            choice = input("\nВыберите действие: ")
            if choice == "1":
                break
            elif choice == "2":
                self.show_inventory()
                break
            else:
                print("Неверный выбор!")

    def show_dungeon_path(self):
        """Показать развилку в подземелье"""
        print(f"\n=== ПОДЗЕМЕЛЬЕ (Этаж {self.floor}/3) ===")
        print(f"Комнат пройдено на этом этаже: {self.rooms_on_current_floor}/{self.ROOMS_PER_FLOOR}")
        print("Перед вами развилка.")

        # Случайно определяем видимость комнат
        left_visible = random.choice([True, False])
        right_visible = random.choice([True, False])

        # Случайно определяем типы комнат
        left_type = random.choice(["враг", "отдых", "сундук"])
        right_type = random.choice(["враг", "отдых", "сундук"])

        # Показываем описание
        left_desc = f"Слева: {self.get_room_description(left_type)}" if left_visible else "Слева: ???"
        right_desc = f"Справа: {self.get_room_description(right_type)}" if right_visible else "Справа: ???"

        print(f"(1) {left_desc}")
        print(f"(2) {right_desc}")

        choice = input("\nКуда пойти? (1-2): ")

        if choice == "1":
            actual_type = left_type
        elif choice == "2":
            actual_type = right_type
        else:
            print("Неверный выбор!")
            return False

        print("\n" + "=" * 40)
        print(f"Вы идете в выбранном направлении...")
        print("=" * 40)

        # Исследуем выбранную комнату
        if actual_type == "враг":
            enemy = Enemy(self.floor)
            return self.battle(enemy)
        elif actual_type == "отдых":
            self.rest_room()
            return True
        elif actual_type == "сундук":
            self.treasure_room()
            return True

    def get_room_description(self, room_type):
        """Получить описание комнаты"""
        descriptions = {
            "враг": "Вы слышите рычание... здесь враг!",
            "отдых": "Тихая комната, можно отдохнуть",
            "сундук": "Блеск в углу... здесь сокровища!"
        }
        return descriptions.get(room_type, "Неизвестная комната")

    def check_floor_completion(self):
        """Проверка завершения этажа"""
        self.rooms_on_current_floor += 1

        if self.rooms_on_current_floor >= self.ROOMS_PER_FLOOR:
            if self.floor < self.MAX_FLOORS:
                self.floor += 1
                self.rooms_on_current_floor = 0
                print("\n" + "=" * 50)
                print(f"=== ВЫ ПРОШЛИ {self.floor - 1} ЭТАЖ! ===")
                print(f"=== ПЕРЕХОДИМ НА ЭТАЖ {self.floor}/3 ===")
                print("=" * 50)
                input("Нажмите Enter, чтобы продолжить...")
            else:
                # Победа!
                return True
        return False

    def victory(self):
        """Экран победы"""
        print("\n" + "=" * 60)
        print("=== ПОБЕДА! ===")
        print("=" * 60)
        print("Вы успешно прошли все 3 этажа подземелья!")
        print("Ваш герой стал легендой!")
        print("\nИтоговые характеристики вашего персонажа:")
        self.player.show_stats()
        print(f"\nВсего собрано монет: {self.player.inventory.get('Монеты', 0)}")
        print(f"Всего пройдено комнат: {self.rooms_cleared}")
        print("\nСпасибо за игру!")
        print("=" * 60)

    def run(self):
        """Запуск игры"""
        print("Добро пожаловать в текстовую RPG!")

        # Сначала создаем персонажа
        self.create_character()

        # Бесконечное исследование подземелья
        while True:
            self.rooms_cleared += 1

            if not self.show_dungeon_path():
                print("\nИгра окончена!")
                restart = input("Начать заново? (да/нет): ").lower()
                if restart == "да":
                    # Сбрасываем игру и создаем нового персонажа
                    self.player = None
                    self.floor = 1
                    self.rooms_cleared = 0
                    self.rooms_on_current_floor = 0
                    self.create_character()
                else:
                    print("Спасибо за игру!")
                    break
            else:
                # Проверяем, завершен ли этаж
                if self.check_floor_completion():
                    self.victory()
                    restart = input("\nНачать заново? (да/нет): ").lower()
                    if restart == "да":
                        # Сбрасываем игру и создаем нового персонажа
                        self.player = None
                        self.floor = 1
                        self.rooms_cleared = 0
                        self.rooms_on_current_floor = 0
                        self.create_character()
                    else:
                        print("Спасибо за игру!")
                        break


if __name__ == "__main__":
    game = Game()
    game.run()