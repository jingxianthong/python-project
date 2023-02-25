
import RPi.GPIO as GPIO
import time


MORSECODEDICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


GPIO.setmode (GPIO.BCM)

GPIO.setwarnings(False)

LIGHT = 47

GPIO.setup(LIGHT,GPIO.OUT)


def dot():
        GPIO.output(LIGHT,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LIGHT,GPIO.HIGH)
        time.sleep(0.2)



def dash():
    GPIO.output(LIGHT,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LIGHT,GPIO.HIGH)
    time.sleep(0.2)

try:
    while True:
        response = input('Enter words: ').upper()
        for letter in response:
            #print(letter)
            moutput = ""
            for symbol in MORSECODEDICT[letter]:
                if symbol == '-':
                    dash()
                    #print(symbol)
                    moutput += symbol + " "

                elif symbol == '.':
                    dot()
                    #print(symbol)
                    moutput += symbol + " "

                else:
                    time.sleep(0.5)
            print("MCode {} : [{}]".format(letter, moutput))        
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()