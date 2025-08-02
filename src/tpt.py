import argparse # Library to parse command line arguments
from datetime import datetime # Library to get the current timestamp
import csv # Library to manipulate csv file
from pathlib import Path

db = Path("testData.csv")

# Parser to interpret command line arguments
parser = argparse.ArgumentParser(
                    prog='tpt',
                    description='Track how much toilet paper you use',
                    epilog='')

# Check if the "database" exist
def check_db():
    if not db.exists():
        with open(db, "w", newline="") as f:
            f.write("timestamp, squares, location, notes\n") # Write the header

# Actually write the entry to the "database"
def write_entry(date, sqr, loc, notes):
    with open(db, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, sqr, loc, notes])

# Add an entry
def add_entry():
    check_db()

    # Define some default variables
    squares = int(0)
    location = str('N/D')
    notes = str('No notes added')

    # Get current date and time
    now = datetime.now()

    # Format date as "day/MonthAbbreviation/year"
    formatted_date = now.strftime("%d/%b/%Y")

    # Get how many square the user used
    print("How many square did you use? :", end="")
    squares = int(input())

    # Get location from the user
    print("Where did you do your business? :", end="")
    location = str(input())

    # Ask the user for notes
    print("Do you want to take any notes about IT? :", end="")
    notes = str(input())

    write_entry(formatted_date, squares, location, notes)
    print(f"Logged: {squares} squares, at {location}. Notes: '{notes}'")

# Display all the stats added until now
def display_stats():
    print("Stats placeholder")

# Command line arguments
parser.add_argument('-a', '--add', required=False, action='store_true', help='Add a new entry.')
parser.add_argument('-s', '--stats', required=False, action='store_true', help='Display the stats you tracked.')

# Parse arguments
args = parser.parse_args()

if args.add:
    add_entry()
if args.stats:
    display_stats()
