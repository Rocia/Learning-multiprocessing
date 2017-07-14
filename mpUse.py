import multiprocessing, os, time
import re
NUMBER_OF_PROCESSES = multiprocessing.cpu_count()

def FindText( host, file_name, text):
    file_size = os.stat(file_name).st_size 
    m1 = open(file_name, "r")

    #work out file size to divide up to farm out line counting

    chunk = (file_size / NUMBER_OF_PROCESSES ) + 1
    lines = 0
    line_found_at = -1

    seekStart = chunk * (host)
    seekEnd = chunk * (host+1)
    if seekEnd > file_size:
        seekEnd = file_size

    if host > 0:
        m1.seek( seekStart )
        m1.readline()

    line = m1.readline()

    while len(line) > 0:
        lines += 1
        if text in line:
            #found the line
            line_found_at = lines
            break
        if m1.tell() > seekEnd or len(line) == 0:
            break
        line = m1.readline()
    m1.close()
    return host,lines,line_found_at

# Function run by worker processes
def worker(input, output):
    for host,file_name,text in iter(input.get, 'STOP'):
        output.put(FindText( host,file_name,text ))

def main(file_name,text):
    t_start = time.time()
    # Create queues
    task_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()
    #submit file to open and text to find
    print ('Starting', NUMBER_OF_PROCESSES, 'searching workers')
    for h in range( NUMBER_OF_PROCESSES ):
        t = (h,file_name,text)
        task_queue.put(t)

    #Start worker processes
    for _i in range(NUMBER_OF_PROCESSES):
        multiprocessing.Process(target=worker, args=(task_queue, done_queue)).start()

    results = {}
    for _i in range(NUMBER_OF_PROCESSES):
        host,lines,line_found = done_queue.get()
        results[host] = (lines,line_found)

    # Tell child processes to stop
    for _i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')

    total_lines = 0
    for h in range(NUMBER_OF_PROCESSES):
        if results[h][1] > -1:
            print (text, 'Found at', total_lines + results[h][1], 'in', time.time() - t_start, 'seconds')
            break
        total_lines += results[h][0]

a = re.compile('<i>([^<]*) v. ([^<]*)</i>([^ ]*)(&lsqb;|\\[)([^\\[]*)(&rsqb;|\\])')

if __name__ == "__main__":
    main( file_name = '11471.txt', text = 'Rickey')

    

