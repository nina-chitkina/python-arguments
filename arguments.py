import argparse
import datetime
import os
parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, 
                        help='says Hi and your name')
parser.add_argument('--lastname', type=str, 
                        help='says Hi and your lastname')  
parser.add_argument('--date', action='store_true',
			 help='shows todays date')
                        
                                 
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


