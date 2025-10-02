from .constants import ROOMS
from .utils import random_event


# Function shows availiable_inventory
def show_inventory(game_state):
    
    """
    Возвращает описание доступного инвентаря.

    Args:
        game_state: текущее состояние игры.

    Returns:
        list: Доступный инвентарь.
    """
    
    
    available_inventory = game_state["player_inventory"]
    if game_state["player_inventory"] != "":
        print(f"Доступный инвентарь: {available_inventory}")
    else:
        print("Инвентарь пуст!")


# Function takes prompt from the player
def get_input(prompt="> "):
    
    """
    Возвращает действие на запрос от пользователя.

    Args:
        prompt: Запрос от игрока.
    """
    
    try:
        user_input = input(prompt)
        return user_input.strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


# Function moves player
def move_player(game_state, direction):
    
    """Перемещает игрока в указанном направлении и обновляет состояние игры."""
    
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]
    next_room = current_room["exits"][direction]

    if direction in current_room["exits"]:
        if next_room == "treasure_room":
            print("Вы попадаете в комнату с оокровищами, проверяем наличие ключа")
            if "rusty_key" in game_state["player_inventory"]:
                print(
                    "Вы используете найденный ключ, "
                    "чтобы открыть путь в комнату сокровищ."
                )
                game_state["steps_taken"] += 1
                game_state["current_room"] = next_room
                random_event(game_state)
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
        else:
            game_state["steps_taken"] += 1
            game_state["current_room"] = current_room["exits"][direction]
            random_event(game_state)
            # describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


# Function to manage items
def take_item(game_state, item_name):
    
    """Добавляет арсеналь в инвентарь игрока и удаляет его из комнаты."""
    
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]
    if item_name in current_room["items"]:
        game_state["player_inventory"].append(item_name)
        current_room["items"].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


# Function to use items
def use_items(game_state, item_name):
    
    """Позволяет игроку использовать доступный инвентарь/сообщает о невозможности."""
    
    if item_name not in game_state["player_inventory"]:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Wow! Стало светлее")
    elif item_name == "sword":
        print("Поздравляем! +1 к вашей уверенности!")
    elif item_name == "bronze_box":
        if "rusty_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("rusty_key")
            print("Вы открыли шкатулку и получили rusty key!")
        else:
            print("У вас уже есть rusty key!")
    elif item_name in [
        "rug",
        "ancient book",
        "treasure chest",
        "sack",
        "rug",
        "Bottle of Dom Perignon",
    ]:
        print("Вообще непонятно, что с этим делать!")
    else:
        print("Неизвестный предмет.")
