"""
The following example shows how to read and parse AIS messages from a file.

When reading a file, the following things are important to know:

- lines that begin with a `#` are ignored
- invalid messages are skipped
- invalid lines are skipped
"""
import serial
import time
from pyais import decode

port = "/dev/ttyACM0"
baud = 9600
line = '!AIVDM,1,1,,A,139m2S?P0BPUjhbL1aw<HOwdR<0`,0*14'

ser = serial.Serial(port, baud)
while True:
    time.sleep(1)

    nbChars = ser.inWaiting()
    if nbChars > 0:
       line = ser.readline()
       #print(line)
       # handelt es sich um eine AIS Nachricht?
       if b'AIVDM' in line:
         # print(nbChars)
         # print(line)
         # Nachricht dekodieren
         decoded = decode(line)
         # print(decoded)
         
         # als dictionary ausgeben
         #as_dict = decoded.asdict()
         #print(as_dict)

         # als json ausgeben
         json = decoded.to_json()
         print(json)
