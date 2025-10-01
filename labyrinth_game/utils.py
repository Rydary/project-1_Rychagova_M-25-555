from .constants import ROOMS
# from .player_actions import get_input

#Function describes current room
def describe_current_room(game_state):
   room_name = game_state['current_room']
   room = ROOMS[room_name]
   
   print(f'Вы находитесь в {room_name.upper()}')
   print(room['description'])
   print(f"Доступные выходы: {', '.join(room['exits'].keys())}")
   if room['items'] != []:
       print(f"Заметные предметы: {', '.join(room['items'])}")
   if room['puzzle'] != None:
       print("Кажется, здесь есть загадка (используйте команду solve).")
   
    
   return {
       'name': room_name,
       'descriprion': room['description'],
       'exits': room['exits'],
       'items': room['items'],
       'puzzle': room['puzzle']
   }
   
#Function to solve puzzles
def solve_puzzle(game_state):
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]
    if current_room['puzzle'] == None:
        print("Загадок здесь нет.")
        return
    else:
        print(current_room['puzzle'][0])
        user_answer = input("Ваш ответ: ")
        if user_answer.strip().lower() == current_room['puzzle'][1]:
            print("Ура! Вы угадали")
            current_room['puzzle'] = None
            game_state['player_inventory'].append('treasure_key')
        else:
            print("Неверно. Попробуйте снова.")
            

#Function to open treasure box
def attempt_open_treasure(game_state):
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]
    if 'treasure_chest' not in current_room['items']:
        print("Сундук уже открыт или отсутствует.")
    else:
        if 'treasure_key' in game_state['player_inventory'] or 'rusty_key' in game_state['player_inventory']:
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            current_room['items'].remove('treasure_chest')
            print("В сундуке сокровище! Вы победили!")
            game_state['game_over'] = True
        else:
            print("Сундук заперт. ... Ввести код? (да/нет)")
            user_answer = input()
            if user_answer.strip().lower() == 'да':
                print(current_room['puzzle'][0])
                code_input = input().strip().lower()
                if code_input == current_room['puzzle'][1]:
                    print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
                    current_room['items'].remove('treasure_chest')
                    print("В сундуке сокровище! Вы победили!")
                    game_state['game_over'] = True
                    return
                else:
                    print("Код неверный, попробуйте снова")
                    print(current_room['puzzle'][0])
            else:
                print("Вы отступаете от сундука.")    
                
                
#Function to help user
def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")