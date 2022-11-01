# Python CLI

Cheatsheet

```py
if __name__ == "__main__":
    import argparse
    parser.add_argument("-n", "--name", help="Please provide the name.")
    args = parser.parse_args()

    name = args.name # if user not input name, this should be None
```

## how to know it is called from CLI?

use `__name__`. If it is `"__main__"`, it is executed from CLI.

```py
print(__name__)

if __name__ == "__main__":
    print("It is executed from CLI.")
else:
    print("It is imported by other file.")
```

## Parse Parameter

```py
import argparse
parser = argparse.ArgumentParser()
# add name parameter to parser
parser.add_argument("-n", "--name", help="Please provide the name.")
args = parser.parse_args()

# get name parameter
name = args.name # if user not input name, this should be None
```

Example

```py
if __name__ == "__main__":
    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", help="Please provide the name.")
    parser.add_argument("-t", "--time", help="Time you want to display.")
    args = parser.parse_args()

    print("Hello {}! It is {}.".format(
        args.name if args.name else "Guest", 
        args.time if args.time else datetime.now().hour))
```

If you run this in CLI:

```bash
$ python practice/test_cli.py

Hello Guest! It is 4.
```

```bash
$ python practice/test_cli.py  -n ubuntu -t 3pm

Hello ubuntu! It is 3pm.
```

```bash
$ python practice/test_cli.py  -h

usage: test_cli.py [-h] [-n NAME] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Please provide the name.
  -t TIME, --time TIME  Time you want to display.
```
