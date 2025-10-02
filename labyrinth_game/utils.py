import math

from .constants import EVENT_PROBABILITY, ROOMS, SCENARIOS_NUM

# from .player_actions import get_input


# Function describes current room
def describe_current_room(game_state):
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    print(f"Вы находитесь в {room_name.upper()}")
    print(room["description"])
    print(f"Доступные выходы: {', '.join(room['exits'].keys())}")
    if room["items"] != []:
        print(f"Заметные предметы: {', '.join(room['items'])}")
    if room["puzzle"]:
        print("Кажется, здесь есть загадка (используйте команду solve).")

    return {
        "name": room_name,
        "descriprion": room["description"],
        "exits": room["exits"],
        "items": room["items"],
        "puzzle": room["puzzle"],
    }


# Function to solve puzzles
def solve_puzzle(game_state):
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]
    if current_room["puzzle"] is None:
        print("Загадок здесь нет.")
        return
    else:
        question = current_room["puzzle"][0]
        main_answer = current_room["puzzle"][1]

        print(question)

        user_answer = input("Ваш ответ: ").strip().lower()
        correct_answers = [main_answer]

        if main_answer == "10":
            correct_answers.extend(["десять", "ten"])
        if main_answer == "морской":
            correct_answers.extend(["морская", "sea"])
        if main_answer == "шаг шаг шаг":
            correct_answers.extend(["шагшагшаг", "step step step", "stepstepstep"])
        if main_answer == "человек":
            correct_answers.extend(["man"])
        if main_answer == "я":
            correct_answers.extend(["я сам", "Я", "me", "i", "myself"])

        if user_answer in correct_answers:
            print("Ура! Вы угадали")
            current_room["puzzle"] = None

            if current_room_name == "hall":
                game_state["player_inventory"].append("treasure_key")
                print("Вы получили в награду treasure key")
            else:
                game_state["player_inventory"].append("rusty_key")
                print("Вы получили в награду rusty key")
        else:
            print("Неверно. Попробуйте снова.")
            if current_room_name == "trap_room":
                trigger_trap(game_state)


# Function to open treasure box
def attempt_open_treasure(game_state):
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]
    if "treasure_chest" not in current_room["items"]:
        print("Сундук уже открыт или отсутствует.")
    else:
        if (
            "treasure_key" in game_state["player_inventory"]
            or "rusty_key" in game_state["player_inventory"]
        ):
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            current_room["items"].remove("treasure_chest")
            print("В сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            print("Сундук заперт. ... Ввести код? (да/нет)")
            user_answer = input()
            if user_answer.strip().lower() == "да":
                print(current_room["puzzle"][0])
                code_input = input().strip().lower()
                if code_input == current_room["puzzle"][1]:
                    print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
                    current_room["items"].remove("treasure_chest")
                    print("В сундуке сокровище! Вы победили!")
                    game_state["game_over"] = True
                    return
                else:
                    print("Код неверный, попробуйте снова")
                    print(current_room["puzzle"][0])
            else:
                print("Вы отступаете от сундука.")


# Function to help user
def show_help(command):
    print("\nДоступные команды:")
    for command, description in command.items():
        print(f" {command:<16} - {description}")


# Function to generate random number
def pseudo_random(seed, modulo):
    value = (math.sin(seed * 12.9898)) * 43758.5453
    return math.floor(((value - math.floor(value))) * modulo)


# Function to gemerate traps
def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state["player_inventory"]
    steps = game_state["steps_taken"]
    if inventory:
        random_index = pseudo_random(steps, len(inventory))
        removed_item = inventory.pop(random_index)
        print(f"Вы потеряли {removed_item}")
    else:
        harm = pseudo_random(steps, EVENT_PROBABILITY)
        if harm < 3:
            game_state["game_over"] = True
            print("Вы попались в ловушку и проиграли!")
        else:
            print("Вы попались в ловушку, но с трудом уцелели! Будьте осторожны!")
            return


# Function to generate random events
def random_event(game_state):
    event_probability = pseudo_random(game_state["steps_taken"], EVENT_PROBABILITY)
    if event_probability == 0:
        define_event = pseudo_random(game_state["steps_taken"] + 1, SCENARIOS_NUM)
        if define_event == 0:  # find coin scenarion
            print("Вы нашли монетку! Coin добавлена в ваш инвентарь")
            game_state["player_inventory"].append("coin")
        elif define_event == 1:  # scare scenario
            print("Вы слышите пугающий шорох")
            if "sword" in game_state["player_inventory"]:
                print("Не бойтесь, у вас есть меч! Вы отпугнули чудовище!")
        elif define_event == 2:  # trap scenario
            if (
                game_state["current_room"] == "trap_room"
                and "torch" not in game_state["player_inventory"]
            ):
                print("Осторожно, вы в ловушке!")
                trigger_trap(game_state)
