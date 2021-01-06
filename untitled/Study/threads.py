import time
import threading


def sleeper(delay):
    time.sleep(delay)
    print("Sleep for {} secs done".format(delay))


### w/o threads

time_start = time.time()
sleeper(5)
print("Time from start: {}".format(time.time() - time_start))
sleeper(4)
print("Time from start: {}".format(time.time() - time_start))


### with threads

print("Run with threads")
time_start = time.time()

t1 = threading.Thread(target=sleeper, args=(5, ))
t2 = threading.Thread(target=sleeper, args=(4, ))
t1.start()
t2.start()

### wait for end threads

t1.join()
t2.join()
print("Time from start: {}".format(time.time() - time_start))



