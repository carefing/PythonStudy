"""
No multi-process:
start to download Modern PHP.pdf...
Modern PHP.pdf download finished! cost 10s
start to download test.mp4...
test.mp4 download finished! cost 5s
total cost 15.00s

Multi-process:
start download process, process id [9856].
start download process, process id [19936].
start to download test.mp4...
start to download Modern PHP.pdf...
test.mp4 download finished! cost 5s
Modern PHP.pdf download finished! cost 8s
total cost 8.16s
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('start download thread, process id [%d].' % getpid())
    print('start to download %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finished! cost %ds' % (filename, time_to_download))

def main():
    # start = time()
    # download_task('Modern PHP.pdf')
    # download_task('test.mp4')
    # end = time()
    # print('total cost %.2fs' % (end - start))

    start = time()
    p1 = Process(target=download_task, args=('Modern PHP.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('test.mp4', ))
    p2.start()
    p1.join() # 等待进程执行结束
    p2.join()
    end = time()
    print('total cost %.2fs' % (end - start))

if __name__ == '__main__':
    main()