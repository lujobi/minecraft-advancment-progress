version = '1.16_20w14a'

mobs = [
    'bee',
    'cat',
    'chicken',
    'cow',
    'fox',
    'horse',
    'llama',
    'mooshroom',
    'ocelot',
    'panda',
    'pig',
    'rabbit',
    'sheep',
    'turtle',
    'wolf'
]


def progress(adv):
    missing = []
    bred_mobs = adv['criteria']
    count = 0
    for mob in mobs:
        if (f'minecraft:{mob}' not in bred_mobs):
            missing.append(mob)
        else:
            count += 1
    msg = 'Progress: [%s/%s], still missing: %s' % (count, len(mobs), missing)
    return msg
