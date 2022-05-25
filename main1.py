import time

from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
class Skip():
    def main(self,num,q):
        for i in range(15):
            j = i**100000
            print(num)
            q.put(num)

class My_Pool():
    def __init__(self, filename, input):
        self.filename = filename
        self.input = input

    def main(self):
        if __name__ == "__main__":
            q = Queue()
            proc0 = Process(target=Skip, args=(self.input[0], q))
            proc1 = Process(target=Skip, args=(self.input[1], q))
            proc2 = Process(target=Skip, args=(self.input[2], q))
            proc3 = Process(target=Skip, args=(self.input[3], q))
            proc4 = Process(target=Skip, args=(self.input[4], q))
            proc5 = Process(target=Skip, args=(self.input[5], q))
            proc6 = Process(target=Skip, args=(self.input[6], q))
            proc7 = Process(target=Skip, args=(self.input[7], q))
            proc8 = Process(target=Skip, args=(self.input[8], q))
            proc9 = Process(target=Skip, args=(self.input[9], q))
            proc10 = Process(target=Skip, args=(self.input[10], q))
            proc0.start()
            proc1.start()
            proc2.start()
            proc3.start()
            proc4.start()
            proc5.start()
            proc6.start()
            proc7.start()
            proc8.start()
            proc9.start()
            proc10.start()
            alive = (proc1.is_alive() or proc0.is_alive() or proc2.is_alive() or proc3.is_alive() or
                     proc4.is_alive() or proc5.is_alive() or proc6.is_alive()
                     or proc7.is_alive() or proc8.is_alive() or proc9.is_alive() or proc10.is_alive())
            while alive or not q.empty():
                if not q.empty():
                    f = open(self.filename, "a", encoding="utf-8")
                    value = q.get(timeout=1)
                    f.write(str(value) + '\n')
                    f.close()
                    alive = (proc1.is_alive() or proc0.is_alive() or proc2.is_alive() or proc3.is_alive() or
                             proc4.is_alive() or proc5.is_alive() or proc6.is_alive()
                             or proc7.is_alive() or proc8.is_alive() or proc9.is_alive() or proc10.is_alive())
                else:
                    continue
pool = My_Pool("text.txt",[0,1,2,3,4,5,6,7,8,9,10])
pool.main()