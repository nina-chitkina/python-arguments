import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, default='friend', 
                        help='says Hi and your name')
parser.add_argument('--lastname', type=str, default='friendson', 
                        help='says Hi and your lastname')           
args = parser.parse_args()

name = args.name
lastname = args.lastname

print(f"Hi, {name[:1]}. {lastname}!")
