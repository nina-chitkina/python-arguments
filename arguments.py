import argparse
import datetime
import os
import random
import string
import base64

parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, 
                        help='says Hi and your name')
parser.add_argument('--lastname', type=str, 
                        help='says Hi and your lastname')  
parser.add_argument('--date', action='store_true',
			 help='shows todays date')
parser.add_argument('--mkdir', type=str, 
                        help='creates directory')   
parser.add_argument('--upper', type=str, 
                        help='uppercase')   
parser.add_argument('--lower', type=str, 
                        help='lowercase') 
parser.add_argument('--upperf', type=str, 
                        help='upper first letter') 
parser.add_argument('--lowerf', type=str, 
                        help='lower first letter') 
parser.add_argument('--random', action='store_true', 
                        help='random letters')  
parser.add_argument('--randomnum', action='store_true', 
                        help='random numbers')    
parser.add_argument('--gitkeep', action='store_true', 
                        help='creates GIT KEEP')                              
parser.add_argument('--encode', type=str, 
                        help='encoding') 
parser.add_argument('--decode', type=str, 
                        help='decoding') 
                                                                  
args = parser.parse_args()

name = args.name
lastname = args.lastname

if args.name and args.lastname:
    print(f"Hi, {name[:1]}. {lastname}!")
elif args.name:
    print(f"Hi, {name}!")
elif args.lastname:
    print(f"Hi, {lastname}!")
if args.date:
    print(f"Today is {datetime.datetime.now()}")
if args.mkdir:
    os.mkdir(args.mkdir)
    print(f"successful")
if args.upper:
    print(f"{args.upper.upper()}")
if args.lower:
    print(f"{args.lower.lower()}")
if args.upperf:
    print(f"{args.upperf.capitalize()}")
if args.lowerf:
    print(f"{args.lowerf[:1].lower()+args.lowerf[1:]}")
    
letters = string.ascii_lowercase
if args.random:
    print(f"{''.join(random.choice(letters) for i in range(10)) }")
numbers = string.digits
if args.randomnum:
    print (f"{''.join(random.choice(numbers) for i in range(6)) }")

if args.gitkeep:
    os.mkdir(".gitkeep")
    print(f"successesful")
    
if args.encode:
    message = args.encode
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
    
if args.decode:
	base64_message = args.decode
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')

	print(message)
    
    
    
    
