import argparse # Library to parse command line arguments
from datetime import datetime # Library to get the current timestamp

# Parser to interpret command line arguments
parser = argparse.ArgumentParser(
                    prog='tpt',
                    description='Track how much toilet paper you use',
                    epilog='')

# Add an entry
def add_entry():
    # Define some default variables
    square = int(0)
    location = str('N/D')
    notes = str('No notes added')

    # Get current date and time
    now = datetime.now()

    # Format date as "day/MonthAbbreviation/year"
    formatted_date = now.strftime("%d/%b/%Y")
    
    # Get how many square the used used
    print("How many square did you use? :", end="")
    square = int(input())

    # Get location from the user
    print("Where did you do your business? :", end="")
    location = str(input())

    # Ask the user for notes
    print("Do you want to take any notes about IT? :", end="")
    notes = str(input())

# Command line arguments
parser.add_argument('-a', '--add', required=False, action='store_true', help='Add a new entry.')

# Parse arguments
args = parser.parse_args()

if args.add:
    add_entry()
