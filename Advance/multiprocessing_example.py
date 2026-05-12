# Multiproccessing example
import multiprocessing 
def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)   
if __name__ == '__main__':
    jobs = []
    for i in range(4, -1, -1):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()