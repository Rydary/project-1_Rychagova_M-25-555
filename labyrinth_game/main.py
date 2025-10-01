#!/usr/bin/env python3

from .constants import ROOMS
from .player_actions import show_inventory, get_input, move_player
from .utils import describe_current_room, solve_puzzle, attempt_open_treasure


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    
    game_state = {
    'player_inventory': [],
    'current_room': 'entrance',
    'game_over': False,
    'steps_taken': 0,
}

    describe_current_room(game_state)

    while not game_state['game_over']:
        command = get_input('Введите команду: ')
        
        if command in ['выход', 'exit', 'quit']:
            print('Игра окончена')
            game_state['game_over'] = True
        elif command == 'осмотреться':
            describe_current_room(game_state)
        elif command in ['north', 'south', 'west', 'east']:
            print(f"Перемещение на {command}...")
            move_player(game_state, command)
        elif command == 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        else:
            print("Неизвестная команда. Попробуйте: осмотреться, solve, выход")
            
#Function to develop all commands from user
# def process_command(game_state, command):
#     command = command.lower().split()
#     match command:
#         case 
                
            
if __name__ == "__main__":
    main()