import argparse # Library for parsing command line arguments
from datetime import datetime # Library for getting the current timestamp
import csv # Library for manipulating csv file
from pathlib import Path # Library for having a path variable
from collections import Counter # Library for counting location stats

db = Path("testData.csv") # Database name/location

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
    formatted_date = now.strftime("%d/%b/%Y %H:%M")

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
    # Define stats variable
    totEntries = int(0) # Total entries
    totSqr = int(0) # Total square used
    avgSqr = float(0) # Average square used
    topLoc = Counter() # Location ranking
    totLoc = int(0) # Total location

    # Read the file and calculate stats
    with open(db, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totEntries += 1 # Calculate the number of entries
            totSqr += int(row["squares"]) # Calculate the number of squares used
            topLoc.update([row["location"]]) # Rank the locations based on frequently used
        avgSqr = float(totSqr / totEntries) # Calculate the average squares used\
        totLoc = len(topLoc.keys()) # Get the total unique location

    # Print stats
    print('🧻 Toilet Paper Stats\n---------------------------------')
    print(f'Total entries: {totEntries}')
    print(f'Total squares used until now: {totSqr}')
    print(f'Average squares used: {avgSqr}')
    print(f'Number of place where you did it: {totLoc}')
    print(f'Top three location where you did it: {topLoc.most_common(3)}')

# Command line arguments
parser.add_argument('-a', '--add', required=False, action='store_true', help='Add a new entry.')
parser.add_argument('-s', '--stats', required=False, action='store_true', help='Display the stats you tracked.')
# TODO: add a subargument to display row data

# Parse arguments
args = parser.parse_args()

if args.add:
    add_entry()
if args.stats:
    display_stats()
