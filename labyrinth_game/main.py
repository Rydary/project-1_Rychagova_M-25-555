#!/usr/bin/env python3

from .constants import COMMANDS
from .player_actions import get_input, move_player, show_inventory, take_item, use_items
from .utils import attempt_open_treasure, describe_current_room, show_help, solve_puzzle


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")

    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    while not game_state["game_over"]:
        command = get_input("Введите команду: ")
        process_command(game_state, command)


# Function to develop all commands from user look, use, go, take, inventory, quit
def process_command(game_state, command):

    command_parts = command.lower().split()

    if not command_parts:
        print("Введите команду: ")
        return

    action = command_parts[0]
    args = command_parts[1:]

    match action:
        case "help":
            show_help(COMMANDS)
        case "look":
            describe_current_room(game_state)
        case "use":
            if args:
                use_items(game_state, args[0])
            else:
                print("Использовать что? Укажите предмет после команды: use предмет")
                return
        case "go":
            if args:
                print(f"Перемещение на {args[0]}...")
                move_player(game_state, args[0])
            else:
                print(
                    "Идти куда? Укажите направление: go (north, south, west, east)"
                )
                return
        case "north" | "south" | "west" | "east":
            print(f"Перемещение на {action}...")
            move_player(game_state, action)
        case "север" | "юг" | "запад" | "восток":
            print(f"Перемещение на {action}...")
            move_player(game_state, action)
        case "take":
            if args:
                take_item(game_state, args[0])
            else:
                print("Взять что? Укажите предмет после команды: take предмет")
                return
        case "inventory":
            show_inventory(game_state)
        case "quit":
            print("Игра окончена")
            game_state["game_over"] = True
        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case _:
            print(
                "Неизвестная команда. Попробуйте: look. use, go, take, inventory, quit"
            )


if __name__ == "__main__":
    main()
