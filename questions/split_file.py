# coding: utf-8

import os
import sys

kilobytes = 1024
megabytes = kilobytes * 1000
#default chunksize
chunksize = int(200 * megabytes)
from_file = ''

def split_file(from_file, to_dir, chunksize=chunksize):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    else:
        for f_name in os.listdir(to_dir):
            os.remove(os.path.join(to_dir, f_name))

    part_num = 0
    f_file = open(from_file, 'rb')
    while True:
        chunk = f_file.read(chunksize)
        if not chunk:
            break

        part_num += 1
        filename = os.path.join(to_dir, 'part%4d' % part_num)
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()

    f_file.close()
    return part_num