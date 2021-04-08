import speech_recognition
import speech_recognition as speech
import serial
from time import sleep
try:
    ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM5'
        ser.timeout = 3
        print(ser)
        ser.open()
except: print('couldnt communicate with arduino on the said port and boudrate')

a1 = speech.Recognizer()
a2 = speech.Recognizer()

with speech.Microphone() as src:
    print('Say the wake word: lift')
    wakeword = a1.listen()

if 'lift' in a1.recognize_google(wakeword):
    print('which floor?')
    with speech.Microphone() as src:
        command = a2.listen(src)
        try:
            floor = a2.recognize_google(command)

        except speech.UnknownValueError:
            print('Sorry, I did not get that, please speak again-')

        except speech.RequestError as e:
            print('Encountered an error:({})' .format(e))
floorlist = floor.split()

units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]

intelligibletext = units + tens + scales

for n in floorlist():
    if n in intelligibletext:
        print('valid number')
    else:
        floorlist.remove(n)

for n in floorlist():
    ser.write(floorlist(n))
    sleep(0.05)




# following code is copied form stackexchange



def text2int(textnum, numwords={}):
    if not numwords:

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

#print text2int("seven billion one hundred million thirty one thousand three hundred thirty seven")
#7100031337
