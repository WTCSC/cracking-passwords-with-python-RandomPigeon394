import argparse
import hashlib
with open('passwords.txt') as g:
    for line in g:
        line = line.strip()
        line.split()
        print(line)
    with open('wordlist.txt') as f:
      for line in f:
        line = line.strip()
        print(f'{hashlib.sha256(line.encode()).hexdigest()} --> {line}')
        white = line.split()
        print(white)
