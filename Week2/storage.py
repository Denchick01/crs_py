import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="Key", default=None)
parser.add_argument("--val", type=str, help="Val", default=None)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.val is None:
   try:
       with open(storage_path, 'r') as f:
           try:
              curr_obj = json.load(f)
           except ValueError:
              print(None)
           else:   
               if args.key in curr_obj:
                   print(', '.join(curr_obj[args.key]))
               else:
                   print(None)
   except FileNotFoundError:
       print(None)
else:
   try:
       with open(storage_path, 'r') as f:
           try:
               curr_obj = json.load(f)
           except ValueError:
               curr_obj = dict()
   except FileNotFoundError:
       curr_obj = dict()

   if args.key in curr_obj:
       curr_obj[args.key].append(args.val)
   else:
       curr_obj[args.key] = [args.val]

   with open(storage_path, 'w') as f:
       json.dump(curr_obj, f)
 

