def show_inventory(game_state):
    available_inventory = game_state['player_inventory']
    if game_state['player_inventory'] != '':
        print(f"Доступный инвентарь: {available_inventory}")
    else:
        print("Инвентарь пуст!")


game_state = {
    'current_room': 'entrance',
    'player_inventory': 'torch'
}

show_inventory(game_state)  