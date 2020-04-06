version = '1.16_20w14a'

foods = [
    'apple',
    'baked_potato',
    'beetroot',
    'beetroot soup',
    'bread',
    'carrot',
    'chorus_fruit',
    'cooked_beef',
    'cooked_chicken',
    'cooked_cod',
    'cooked_mutton',
    'cooked_porkchop',
    'cooked_rabbit',
    'cooked_salmon',
    'cookie',
    'dried_kelp',
    'enchanted_golden_apple',
    'golden_apple',
    'golden_carrot',
    'honey_bottle',
    'melon',
    'mushroom_stew',
    'poisonous_potato',
    'potato',
    'pufferfish',
    'pumpkin_pie',
    'rabbit_stew',
    'raw_beef',
    'raw_chicken',
    'raw_cod',
    'raw_mutton',
    'raw_porkchop',
    'raw_rabbit',
    'raw_salmon',
    'rotten_flesh',
    'spider_eye',
    'suspicious_stew',
    'sweet_berries',
    'tropical_fish'
]


def progress(adv):
    missing = []
    eaten_foods = adv['criteria']
    count = 0
    for food in foods:
        if (f'{food}' not in eaten_foods):
            missing.append(food)
        else:
            count += 1
    msg = 'Progress: [%s/%s], still missing: %s' % (count, len(foods), missing)
    return msg
