import os
import time
import csv

def convert_to_uppercase_and_measuretime(file_count):
    start_time = time.time()

    for _ in range(file_count):
        pass
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    return elapsed_time

file_counts = [100,200,300,400,500]


csv_file = "execution_times.csv"

with open(csv_file, mode="w", newline="") as csvfile:
    fieldnames = ["No. of Files", "Time Taken (sec)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for file_count in file_counts:
        elapsed_time = convert_to_uppercase_and_measuretime(file_count)
        writer.writerow({"No. of Files": file_count, "Time Taken (sec)": elapsed_time})
        print(f"{file_count} | {elapsed_time} seconds")

print(f"Results saved in '{csv_file}'.")
