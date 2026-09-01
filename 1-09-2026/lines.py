#my attempt at doing something to making that zig-zag

import time , sys
try:

    while True:
        for i in range(8,18):
            print('-' *(i*i))
            time.sleep(0.1)

        for i in range(18 , 1 , -1):
            print ('*' * (i*i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()