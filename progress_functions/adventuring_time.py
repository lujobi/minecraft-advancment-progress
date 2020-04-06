version = '1.16_20w14a'

biomes = [
    'badlands',
    'badlands_plateau',
    'bamboo_jungle',
    'bamboo_jungle_hills',
    'beach',
    'birch_forest',
    'birch_forest_hills',
    'cold_ocean',
    'dark_forest',
    'deep_cold_ocean',
    'deep_frozen_ocean',
    'deep_lukewarm_ocean',
    'desert',
    'desert_hills',
    'forest',
    'frozen_river',
    'giant_tree_taiga',
    'giant_tree_taiga_hills',
    'jungle',
    'jungle_edge',
    'jungle_hills',
    'lukewarm_ocean',
    'mountains',
    'mushroom_field_shore',
    'mushroom_fields',
    'plains',
    'river',
    'savanna',
    'savanna_plateau',
    'snowy_beach',
    'snowy_mountains',
    'snowy_taiga',
    'snowy_taiga_hills',
    'snowy_tundra',
    'stone_shore', 
    'swamp',
    'taiga',
    'taiga_hills',
    'warm_ocean',
    'wooded_badlands_plateau',
    'wooded_hills',
    'wooded-mountains'
]


def progress(adv):
    missing = []
    visited_biomes = adv['criteria']
    count = 0
    for biome in biomes:
        if (f'minecraft:{biome}' not in visited_biomes):
            missing.append(biome)
        else:
            count += 1
    msg = 'Progress: [%s/%s], still missing: %s' % (count, len(biomes), missing)
    return msg
