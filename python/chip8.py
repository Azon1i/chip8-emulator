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

def frstn(instr):  # first nibble instruction
    instr >>= 12
    instr &= 0xF
    return instr

def scndn(rgs): # second nibble register
    rgs >>= 8
    rgs &= 0xF
    return rgs

def thrdn(rgs): # third nibble register
    rgs >>= 4
    rgs &= 0xF    
    return rgs

def N(data): # mask last nibble
    data &= 0xF
    return data

def NN(data): # mask last 2 nibbles
    data &= 0xFF
    return data

def NNN(data): # mask last 3 nibbles
    data &= 0xFFF
    return data



#def fstN(n):
#    cnt = fetch(n)
#    cnt = cnt << 12
#    cnt = cnt | 0x0000
#    return cnt

apply_fonts()
read()

counter = 0x200
print(hex(fetch(counter)))

def six_eyes(value_in_hex):
    r1 = frstn(value_in_hex)
    r2 = scndn(value_in_hex)
    r3 = thrdn(value_in_hex)
    r4 = N(value_in_hex)
    r5 = NN(value_in_hex)
    r6 = NNN(value_in_hex)

    print(hex(value_in_hex) + " so it's :" ,end=" ")
    print(hex(r1),end=" ")
    print(hex(r2),end=" ")
    print(hex(r3),end=" ")
    print(hex(r4),end=" ")
    print(hex(r5),end=" ")
    print(hex(r6),end="\n")

six_eyes(0x6A2F)
six_eyes(0xD123)
six_eyes(0x00E0)


#while True :

    

    #n =int(input("choose your starting address"))
    #mem[n] = int(input("write 1st value"))
    #mem[n+1] = int(input("write 2nd value"))
    #print(hex(fetch(n)))






