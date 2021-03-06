import logparser
from render import render_excited_states
import argparse
import os

def main():
    args = input_args()

    states = logparser.parse_log(args.logfile)

    if args.title:
        print("\n " + args.title)
    else:
        print("\n Excited states from '{}'".format(os.path.basename(args.logfile)))
    render_excited_states(states)
    print("")

#Parses and prepares input arguments.
def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("logfile")
    parser.add_argument("-t", "--title", help="Adds a title to the table")
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    main()