from multiprocessing import Process, Pipe

def A(conn,name):
    conn.send([123, None, 'Hey',name])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    process = Process(target=A, args=(child_conn,'Alloy',))
    process.start()
    print (parent_conn.recv())
    process.join()
'''
Output:-

[123, None, 'Hey', 'Alloy']
'''