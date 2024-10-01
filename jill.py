import argparse
import hashlib
#First we import hash and argparse to open our files 
parser = argparse.ArgumentParser(description='hashing lines in a file.')
#I added 2 arguments because we had 2 files we were comparing to eachother
parser.add_argument('filename', help='The file to hash lines from')
parser.add_argument('filename2', help='The file to hash lines from')
args = parser.parse_args()
#Next I make sure to open the file num 1 and set a variable which I did g
with open(args.filename) as g:
#Next I said for the lines in g strip the white spaces and split by the colon which gives me the username and hash seperately 
    for line in g:
        line = line.strip()
        line = line.split(":")
#Next open the file num2 and also use .strip to get rid of whitespaces
        with open(args.filename2) as f:
          for word in f:
            word = word.strip()
#After that I hash all of the words and set it as a variable 
            hash = hashlib.sha256(word.encode()).hexdigest()
#Lastly for the hashed words match it with the hashes from the other file and match with their name
            if hash == line[1]:
              print(f'{line[0]}:{word}')
