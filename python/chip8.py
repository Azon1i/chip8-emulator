from pathlib import Path
import sys

main = Path(__file__).parent.parent / "ROM" / "ibm.ch8"



mem=[0] * 4096 # total memory bytes


display_x=64 #display width
display_y=32 #display height
screen=bytearray(2048)
deLay=0 #timer value
S_deLay=0 #sound timer value

counter=0x200
i = 0x00 #pointer

vx=0x0  #2nd nibble selector
vy=0x0 #3rd nibble selector

stack = [0] * 16
istack = 0 #pointer for the stack

reg = [0] * 16
rdADD= 0x200
fsADD= 0x050 # fonts start address
fonts = [
    0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
    0x20, 0x60, 0x20, 0x20, 0x70, # 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
    0x90, 0x90, 0xF0, 0x10, 0x10, # 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
    0xF0, 0x10, 0x20, 0x40, 0x40, # 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
    0xF0, 0x90, 0xF0, 0x90, 0x90, # A
    0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
    0xF0, 0x80, 0x80, 0x80, 0xF0, # C
    0xE0, 0x90, 0x90, 0x90, 0xE0, # D
    0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
    0xF0, 0x80, 0xF0, 0x80, 0x80  # F
]

keyboard_codespace = [45,2,3,4,16,17,18,30,31,32,44,46,5,19,33,47] #the codespace for keys which are 123C 456D 789E A0BF -> 1234 QWER ASDF ZXCV 

def apply_fonts():
    for idx, val in enumerate(fonts, start=fsADD): # font indexer in memory
        mem[idx] = val

def read():
    size= main.stat().st_size
    if size > 3584:
        sys.exit("Error 67 ROM too large")
    else:
        data= main.read_bytes()
        for idx, val in enumerate(data, start=rdADD):
            mem[idx] = val
        print("reading done")
    

def fetch(n):
    cnt = mem[n]
    cnt = cnt << 8
    cnt = cnt | mem[n+1]
    return cnt

#def fstN(n):
#    cnt = fetch(n)
#    cnt = cnt << 12
#    cnt = cnt | 0x0000
#    return cnt

apply_fonts()
read()


counter = 0x200
print(hex(fetch(counter)))

#while True :

    

    #n =int(input("choose your starting address"))
    #mem[n] = int(input("write 1st value"))
    #mem[n+1] = int(input("write 2nd value"))
    #print(hex(fetch(n)))






