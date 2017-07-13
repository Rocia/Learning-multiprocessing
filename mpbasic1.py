from multiprocessing import Pool

def f(x):
    return x**3

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1,5,7]))

'''
Output:-
 
[1, 125, 343]
 '''