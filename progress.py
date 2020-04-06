import json
from progress_functions import functions as progress_functions

import advancement_utils as adv_utils


def check(current):
    notStarted = []
    inProgress = []
    finished = []

    for category in adv_utils.getCategories():
        for advancement in adv_utils.getAdvancements(category):
            try:
                adv_prog = current[f'minecraft:{category}/{advancement}']
                if (adv_prog['done']):
                    finished.append(adv_utils.getAdvancement(category, advancement))
                else:
                    if (advancement in progress_functions):
                        inProgress.append({**adv_utils.getAdvancement(category, advancement), 'progress': progress_functions[advancement](adv_prog)})
                    else:
                        inProgress.append(adv_utils.getAdvancement(category, advancement))
            except:
                notStarted.append(adv_utils.getAdvancement(category, advancement))
    return {'notStarted': notStarted, 'inProgress': inProgress, 'finished': finished}