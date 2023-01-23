import multiprocessing as mp
from multiprocessing import Process
import time

# def sub_process(name):
#     print("[sub] start")
#     print(name)
#     cp = mp.current_process()
#     print(f"[sub] pid : {cp.pid}")
#     print("[sub] end")


# if __name__ == "__main__":
#     print("[main] start")
#     p = mp.Process(target=sub_process, args=("startcoding",))
#     p.start()
#     cp = mp.current_process()
#     print(f"[main] pid : {cp.pid}")
#     print("[main] end")

class Subprocess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")


if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name="startcoding")
    p.start()
    time.sleep(1)
    if p.is_alive():
        p.terminate()
    print("[main] end")
