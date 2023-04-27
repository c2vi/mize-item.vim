import sys

# Why can't I find "python RedirectStream" on google, to know from where to import it??
#sys.stdout = RedirectStream(lambda data: nvim.async_call(nvim.out_write, data))

def write_buffer(content):
    vim.current.buffer[:] = content

old_print = print
def myprint(*args):
    vim.async_call(old_print, "VIM: ", *args)

global file
file = open("./log", "w")

class MyOUT_to_nvim_python_is_stupid():
    #def __init__(self):

    def write(self, data):
        global file
        file.write(data)
        file.flush()

        #vim.async_call(old_print, "VIM: " + data)
            #file = open("./log", "w")
            #file.close()
        #data = "VIM" + data
        #vim.async_call(write_buffer, data.split("\n"))
        

sys.stdout = MyOUT_to_nvim_python_is_stupid()

# redirecting stdout to somewhere else for testing, bc in vim you don't see all prints
#sys.stdout = open("./log", "a")

#builtins.print = myprint

import time
import asyncio
import vim
from pymize import Client, Item
import json
from threading import Thread

def python_anonymous_function(update):
    string = json.dumps(update["new"].main, indent=4)
    vim.async_call(write_buffer, string.split("\n"))


def open_item(ID):
    sys.stdout.write("start????\n")
    global client
    client = Client()

    global item

    client.add_get_item_callback(ID, get_item)

    msg = {
            "cmd": "item.get-sub",
            "id": "0",
    }
    client.sock.send("hello")
    return
    client.send(msg)


    #client.add_update_callback(ID, python_anonymous_function)


def get_item(item_hi):
    global item
    item = item_hi
    string = json.dumps(item.main, indent=4)
    vim.async_call(write_buffer, string.split("\n"))


def terminate_thread():
    global file
    global client
    client.sock.close()
    #sleep(0.5)
    file.close()
    exit()

def update_item():
    global item
    string = "\n".join(vim.current.buffer)
    try:
        dic = json.loads(string)
    except:
        print("Not valid JSON")
        return
    new_item = Item(dic)
    print("writing")
    client.update_item(new_item, "client")



