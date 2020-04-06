import argparse
import json
from termcolor import colored
import textwrap


import progress
import advancement_utils as adv_utils
from progress_functions import versions as function_versions

preferredWidth = 120


def formatFinished(array):
    msg = 'Finished %s: \n  -%s' % (len(array),
                                    '\n  -'.join(map(lambda x: x['advancement'], array)))
    return msg


def formatFancy(array, verbose=False):
    prefix = '       '
    wrapper = textwrap.TextWrapper(
        initial_indent=prefix, width=preferredWidth, subsequent_indent=' '*len(prefix))

    def formatInfo(info, desc):
        wrapped = wrapper.fill(desc) if desc else ''
        res = f'{info}: \n{wrapped}'
        return res

    def format(x):
        progress = 'No progress info'
        try:
            progress = x['progress']
        except:
            pass

        res = '%s: \n     %s\n     %s\n     %s\n     %s' % (
            x['advancement'],
            formatInfo('Parent', x['parent']),
            formatInfo('In-game description', x['in_game_description']),
            formatInfo('Actual requirements', x['actual_requirements'] if x['actual_requirements'] else 'None'),
            formatInfo('Progress', progress)
        ) if verbose else (
            '%s: \n     %s' % (
                x['advancement'],
                formatInfo('In-game description', x['in_game_description']),
            ))

        return res

    msg = '\n\nIn Progress %s: \n  -%s' % (len(array),
                                           '\n\n  -'.join(map(format, array)))
    return msg


def checkVersions():
    version = adv_utils.getMeta()['minecraft-version']
    for key, v in function_versions.items():
        if v != version:
            return key
    return True

def main(own_file, verbose):
    print("Welcome using the my Advancement Progress Tool")
    print(adv_utils.getMeta())

    if not checkVersions() == True:
        print(colored("versions of functions in %s.py don\'t match" % (checkVersions()), 'red'))
        return

    print(colored("Version check successful \n ", 'green'))

    with open(own_file) as file:
        own = json.load(file)
        result = progress.check(own)
        print(colored(formatFinished(result['finished']), 'green'))
        print(colored(formatFancy(result['notStarted'], verbose), 'red'))
        print(colored(formatFancy(result['inProgress'], True), 'yellow'))
        print(colored('\nOverall progress: %s finished, %s in progress, %s not started of total %s' % (
            len(result['finished']), 
            len(result['inProgress']), 
            len(result['notStarted']), 
            len(result['finished']) + len(result['inProgress'])+len(result['notStarted'])
        ), 'blue'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='advancement file including the .json-ending')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    args = parser.parse_args()
    main(args.file, args.verbose)
