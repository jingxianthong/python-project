#diyprojectslab.com
 
import machine
import utime

MORSECODEDICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'} # / <-- this symbol is use for spacebar


led = machine.Pin("LED", machine.Pin.OUT)
led.off()

count = 0

def dot():
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
    
    
def dash():
    led.value(1)
    utime.sleep(3)
    led.value(0)
    utime.sleep(1)
    
while True:
    response = ('SOS').upper()
    for letter in response:
        moutput = ""
        for symbol in MORSECODEDICT[letter]:
            if symbol == '-':
                dash()
                moutput += symbol + " " 
                
            elif symbol == '.':
                dot()
                moutput += symbol + " "
                
            else:
                utime.sleep(2)
                
        print("MCode {} : [{}]".format(letter, moutput))        
        utime.sleep(2) 