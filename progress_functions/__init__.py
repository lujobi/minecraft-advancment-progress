from .kill_all_mobs import *
from .adventuring_time import *
from .balanced_diet import *
from .bred_all_animals import *
from .complete_catalogue import *

functions = {
    'kill_all_mobs': kill_all_mobs.progress,
    'adventuring_time': adventuring_time.progress,
    'balanced_diet': balanced_diet.progress,
    'bred_all_animals': bred_all_animals.progress,
    'complete_catalogue': complete_catalogue.progress,
}

versions = {
    'kill_all_mobs': kill_all_mobs.version,
    'adventuring_time': adventuring_time.version,
    'balanced_diet': balanced_diet.version,
    'bred_all_animals': bred_all_animals.version,
    'complete_catalogue': complete_catalogue.version,
}