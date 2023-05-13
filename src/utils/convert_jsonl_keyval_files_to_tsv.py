import glob
import json
import sys
import csv
import time
import os, errno
def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred
#Path of the jsonl file
dir_path = sys.argv[1]#'path-to-folder-that-contains-jsonl-files'
#Reading all of jsonl files
files = [f for f in glob.glob(dir_path + "**/*.jsonl", recursive=True)]
for cnt, f in enumerate(files):
    output_path = str(f).replace('jsonl', 'csv')
    silentremove(output_path)
    print("{}) output_path: {}".format(cnt, output_path))
    with open(f, 'r') as lines:
        for line in lines:
            data = json.loads(line)
            with open(output_path, 'a' , newline='') as f:
                f.write("{}\t{}\n".format(data[list(data.keys())[0]], data[list(data.keys())[1]]))
