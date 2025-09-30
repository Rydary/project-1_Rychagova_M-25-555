from constants import ROOMS

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
   
   
game_state = {
    'current_room': 'basement',
    'player_inventory': 'torch'
}

describe_current_room(game_state)