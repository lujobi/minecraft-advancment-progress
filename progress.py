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
                msg = '%s: %s, %s' %(advancement, adv_prog['done'], (progress_functions[advancement](adv_prog) if advancement in progress_functions else False))
                print(msg)
                if (adv_prog['done']):
                    finished.append(adv_utils.getAdvancement(category, advancement))
                else:
                    inProgress.append(adv_utils.getAdvancement(category, advancement))
                    if (advancement in progress_functions):
                        inProgress[-1]['progress'] = progress_functions[advancement](adv_prog)
            except:
                notStarted.append(adv_utils.getAdvancement(category, advancement))
    return {"notStarted": notStarted, "inProgress": inProgress, "finished": finished}