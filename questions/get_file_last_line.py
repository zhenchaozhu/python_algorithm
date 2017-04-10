# coding: utf-8

import os

def get_file_last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    buf_size = 1024
    with open(inputfile, 'rb') as f:
        last_line = ''
        if filesize > buf_size:
            max_seed_point = filesize // buf_size
            f.seek((max_seed_point - 1) * buf_size)
        else:
            f.seek(0, 0)

        lines = f.readlines()
        if lines:
            lineno = 1
            while last_line == "":
                last_line = lines[-lineno].strip()
                lineno += 1

        return last_line