import sys
import itertools
import csv

# Create a Logisim ROM file for my RISC-V 32I video series based on the truth table located at
# https://docs.google.com/spreadsheets/d/1vEK9cUZK4V5SEFH1DbEvg8QJjkaMn-dQ8DxfBNaIYIs/edit?usp=sharing
# Usage: python buildrom.py < tt.csv > control.rom
if __name__ == '__main__':
  words = []

  # Create a 512 list (9 bits) mapping to 5 bits of control data output
  for x in range(512):
    words.append(0)

  # Create an iterator to chop off first record of truth table
  iter = itertools.islice(sys.stdin, 1, None)

  # Open the truth table csv file
  csv_reader = csv.DictReader(iter)

  # Process logic table rows
  for row in csv_reader:
    words[int(row["ihex"], 16)] = int(row["ohex"], 16)

  # Need to write words in 16 byte rows, hex formatted
  print("v3.0 hex words plain")
  for x in range(int(512/16)):
    line = ""
    # Iterate over each word
    for y in range(16):
      line += f"{words[(x*16) + y]:0>2x} "
    # Chop off the last space
    line = line[:-1]
    print(line)
  