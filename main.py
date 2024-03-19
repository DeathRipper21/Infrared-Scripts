import time
import gc
from machine import Pin, freq
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8, NEC_16, SAMSUNG
from ir_tx.nec import NEC
#import _thread
import sys
import neopixel

global replays
replays=[]
global np
np=neopixel.NeoPixel(Pin(23),10)
button = Pin(24, Pin.IN, Pin.PULL_UP)
p = Pin(17, Pin.IN)
global nec
nec = NEC(Pin(0, Pin.OUT, value = 0))

def cb(data, addr, ctrl):
    if data < 0:
        print("Repeat code.")
    else:
        print(f"Data:{data} Address:{addr} Control:{ctrl}")
        print(replays)
        if [addr, data] in replays or addr and data != int:
            pass
        else:
            replays.append([addr, data])
            
def listen_IR(): #proto=0
    classes = (NEC_8,NEC_16,SAMSUNG)
    #nec = NEC(Pin(0, Pin.OUT, value = 0))
    ir = classes[0](p, cb)
    ir.error_function(print_error)
    ir.verbose = True
    try:
        while True:
            print("Receiving...")
            time.sleep(1)
            gc.collect()
    except KeyboardInterrupt:
        ir.close()
    except Exception as e:
        ir.close()

def replay_all_IR(button):
    print(replays)
    np[0]=(255,0,0)
    np.write()
    try:
        while True:
            if len(replays) > 0:
                print("Sending codes")
                time.sleep(3)
                if type(replays[-1][0]) != int or type(replays[-1][1]) != int:
                    print("Issue")
                    pass
                else:
                    for i in range(0, len(replays)):
                        nec.transmit(replays[i][0], replays[i][1])
                        time.sleep(3)
                    break
                    np[0]=(0,255,0)
                    np.write()
            else:
                np[0]=(0,255,0)
                np.write()
                break
    except Exception as e:
        print(e)


def replay_IR(button):
    np[0]=(255,0,0)
    np.write()
    try:
        while True:
            if len(replays) > 0:
                print("Sending codes")
                time.sleep(1)
                if type(replays[-1][0]) is not int or type(replays[-1][1]) is not int:
                    print("Issue")
                    pass
                else:
                    if type(replays[-1][0]) == int and type(replays[-1][1]) == int:
                        nec.transmit(replays[-1][0], replays[-1][1])
                    break
                    np[0]=(0,255,0)
                    np.write()
            else:
                np[0]=(0,255,0)
                np.write()
                break
    except Exception as e:
        print(e)
        
def brute_force():
    np[0]=(255,0,0)
    np.write()
    try:
        address = 0
        while address < 257:
            for i in (range(0, 257)):
                if i == 256:
                    address+=1
                if type(address) != int or type(i)!= int:
                    pass
                else:
                    print("Success!")
                    nec.transmit(address, i)
                #print(address,i)
                time.sleep(1)
        np[0]=(0,255,0)
        np.write()
    except Exception as e:
        print(e)



np[0]=(0,255,0)
np.write()
button.irq(trigger=Pin.IRQ_FALLING, handler=replay_IR)
listen_IR()
#replay_IR()
#replay_all_IR()
#brute_force()
