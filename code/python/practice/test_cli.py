print(__name__)

if __name__ == "__main__":
    print("It is executed from CLI.")

    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", help="Please provide the name.")
    parser.add_argument("-t", "--time", help="Time you want to display.")
    args = parser.parse_args()

    print("Hello {}! It is {}.".format(
        args.name if args.name else "Guest", 
        args.time if args.time else datetime.now().hour))
else:
    print("It is imported by other file.")

