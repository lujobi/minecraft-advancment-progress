import argparse
import json

import progress
import advancement_utils as adv_utils


def main(own_file):
    print(adv_utils.getMeta())
    with open(own_file) as file:
        own = json.load(file)
        progress.check(own)
        #print(progress.check(own))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="advancement file")
    args = parser.parse_args()
    main(args.file)