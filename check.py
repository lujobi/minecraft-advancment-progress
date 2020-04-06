import argparse




def main(file):
    with open(file) as file:
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="advancement file")
    args = parser.parse_args()
    main(args.file)