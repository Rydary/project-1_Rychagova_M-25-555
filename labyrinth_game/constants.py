# labyrinth_game/constants.py
ROOMS = {
    "entrance": {
        "description": "Вы в темном входе лабиринта...",
        "exits": {"north": "hall", "east": "trap_room"},
        "items": ["torch"],
        "puzzle": None,
    },
    "hall": {
        "description": "Большой зал с эхом. По центру стоит пьедестал "
        " с запечатанным сундуком.",
        "exits": {"south": "entrance", "west": "library", "north": "treasure_room"},
        "items": [],
        "puzzle": (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". '
            'Введите ответ цифрой или словом.',
            "10",
        ),
    },
    "trap_room": {
        "description": 'Комната с хитрой плиточной поломкой. На стене видна надпись: '
        '"Осторожно — ловушка".',
        "exits": {"west": "entrance"},
        "items": ["rusty_key"],
        "puzzle": (
            'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд '
            '(введите "шаг шаг шаг")',
            "шаг шаг шаг",
        ),
    },
    "library": {
        "description": "Пыльная библиотека. На полках старые свитки. "
        "Где-то здесь может быть ключ от сокровищницы.",
        "exits": {"east": "hall", "north": "armory"},
        "items": ["ancient book"],
        "puzzle": (
            'В одном свитке загадка: "Какой болезнью не болеют на суше?" ',
            "морской",
        ),
    },
    "armory": {
        "description": "Старая оружейная комната. "
        "На стене висит меч, рядом — небольшая бронзовая шкатулка.",
        "exits": {"south": "library"},
        "items": ["sword", "bronze box"],
        "puzzle": None,
    },
    "treasure_room": {
        "description": "Комната, на столе большой сундук. "
        "Дверь заперта — нужен особый ключ.",
        "exits": {"south": "hall"},
        "items": ["treasure_chest"],
        "puzzle": (
            "Дверь защищена кодом. Введите код "
            "(подсказка: это число пятикратного шага, 2*5= ? )",
            "10",
        ),
    },
    "basement": {
        "description": "Холодный подвал, в углу которого лежит загадочный мешок",
        "exits": {"west": "treasure_room", "north": "wine_cellar"},
        "items": ["sack"],
        "puzzle": (
            "Ответьте: утром на четырех ногах, днем - на двух, вечером - на трех",
            "человек",
        ),
    },
    "fireplace_room": {
        "description": "Небольшая уютная комната, стены покрыты коврами, пылает камин.",
        "exits": {"south": "treasure_room"},
        "items": ["rug"],
        "puzzle": None,
    },
    "wine_cellar": {
        "description": "Огромный погреб, наполненный сотнями бутылок вина.",
        "exits": {"west": "fireplace_room", "south": "basement"},
        "items": ["Bottle of Dom Perignon"],
        "puzzle": ("Отгадайте загадку: сын моего отца, но мне не брат?", "я"),
    },
}

EVENT_PROBABILITY = 10

SCENARIOS_NUM = 3

COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреться вокруг и понять, в какой комнате вы находитесь",
    "use <item>": "использовать предмет (sword/rusty_key/torch/treasure_key)",
    "take <item>": "добавить предмет в инвентарь (sword/rusty_key/torch/treasure_key)",
    "inventory": "посмотреть доступный инвентарь",
    "quit": "выйти из игры",
    "help": "показать это сообщение",
}
