#!/usr/bin/env python

from pymize import Client, Item
from threading import Thread
from queue import Queue
from time import sleep
import signal
import sys

def other(queue):
    sleep(1)
    queue.put("hello")

#q = Queue()
#thread = Thread(target=other, args=(q,))
#thread.start()

#msg = q.get()
#q.task_done()
#print("GOT: ", msg)

def signal_handler(sig, frame):
    client.sock.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def pr(update):
    print("Update: ", update)

client = Client()
item = client.get_item("0")
item.main["hi"] = 3
client.add_update_callback(item.id, pr)
client.update_item(item, "client")




