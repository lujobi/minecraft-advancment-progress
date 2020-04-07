version = '1.16_20w14a'

cats = ['tabby', 'tuxedo', 'red', 'siamese', 'british_shorthair', 'calico', 'persian', 'ragdoll', 'white', 'black.'
]



def progress(adv):
    missing = []
    tamed_cats = adv['criteria']
    count = 0
    for cat in cats:
        if (f'textures/entity/cat/{cat}.png' not in tamed_cats):
            missing.append(cat)
        else:
            count += 1
    msg = 'Progress: [%s/%s], still missing: %s' % (count, len(cats), missing)
    return msg
