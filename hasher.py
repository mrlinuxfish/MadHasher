#!/usr/bin/env python3

import os
import itertools
from colorama import Fore
print(Fore.GREEN)
print()
print("Types of hash codes: md5sum, sha256sum, etc.")
print()
type = str(input("Enter Hash Type: "))
print()

for i in itertools.count(1,1):
    password = str(input(f"Enter Pasword#{i}: "))
    maker = os.system(f'echo -n "{password}" | {type} >> HashFile_{type}.txt')
