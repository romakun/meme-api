from faker import Faker
import random

MEME_URLS = [
    'https://9gag.com/gag/awy0Zy1',
    'https://9gag.com/gag/aD2AYWO',
    'https://9gag.com/gag/azxgeBN',
    'https://9gag.com/gag/an7qzen',
    'https://9gag.com/gag/a5QeXnV'
]


def generate_meme_body():
    return {
        "info": {
            "colors": [
                Faker().color(),
                Faker().color(),
                Faker().color()
            ],
            "objects": [
                Faker().word(),
                Faker().word()
            ]
        },
        "tags": [
            Faker().word(),
            Faker().word(),
            Faker().word()
        ],
        "text": Faker().text(),
        "url": random.choice(MEME_URLS)
    }
