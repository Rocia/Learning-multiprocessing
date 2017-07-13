import multiprocessing, time, signal

p = multiprocessing.Process(target=time.sleep, args=(1000,))

print (p, p.is_alive())
p.start()
print (p, p.is_alive())
p.terminate()
time.sleep(0.1)
print (p, p.is_alive())
p.exitcode == -signal.SIGTERM

'''
Output:-

<Process(Process-1, initial)> False
<Process(Process-1, started)> True
<Process(Process-1, stopped[SIGTERM])> False
'''