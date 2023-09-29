import os
import random
import string
import time

directory = "random_text_files"

if not os.path.exists(directory):
    os.makedirs(directory)
    
def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

num_files = 50

num_lines = 20000

start_time = time.time()
for file_num in range(1, num_files+1):
    file_name = os.path.join(directory, f"file_{file_num}.txt")

    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            line = random_string(20)
            file.write(line + '/n')
            
end_time = time.time()
elapsed_time = end_time-start_time

print(f"{num_files} files with each {num_lines} lines have been created in the {directory} directory")

print(elapsed_time)
            