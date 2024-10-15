

import os

# listing the directory
files = os.listdir('cluttredFolder')


i = 0

# looping through all file to rename
for file in files:
    if file.endswith('png'):
        print(file)
        os.rename(f'cluttredFolder/{file}' , f'cluttredFolder/{i}.png')
        i = i + 1
