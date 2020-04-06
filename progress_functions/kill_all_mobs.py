version = '1.16_20w14a'

mobs = [
    'blaze',
    'cave Spider',
    'creeper',
    'drowned',
    'enderman',
    'evoker',
    'ghast',
    'guardian',
    'husk',
    'magma_cube',
    'phantom',
    'pillager',
    'ravager',
    'shulker',
    'silverfish',
    'skeleton',
    'slime',
    'spider',
    'stray',
    'vindicator',
    'witch',
    'wither_skeleton',
    'zombie',
    'zombie_pigman',
    'zombie_villager',
    'elder_guardian',
    'enderdragon',
    'endermite',
    'hoglin',
    'piglin',
    'vexe',
    'wither',
    'zoglin'
]



def progress(adv):
    missing = []
    killed_mobs = adv['criteria']
    count = 0
    for mob in mobs:
        if (f'minecraft:{mob}' not in killed_mobs):
            missing.append(mob)
        else:
            count += 1
    msg = 'Progress: [%s/%s], still missing: %s' % (count, len(mobs), missing)
    return msg
