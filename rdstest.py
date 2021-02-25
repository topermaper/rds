import serial
import sys

#baudratelist = [1200, 2400, 4800, 19200, 38400, 57600, 115200]
#paritylist = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE]
#stopbitlist = [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]
#bytesizelist = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]

CR = "\n"
LF = "\r"

class RdsTest(object):


    def __init__(self):
        print("Initializing RDS comms:")

        self.baudrate = 19200
        self.parity   = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE_POINT_FIVE
        self.bytesize = serial.EIGHTBITS

        print("BAUD RATE={} PARITY={} STOPBITS={} BYTESIZE={}".format(str(self.baudrate),str(self.parity),str(self.stopbits),str(self.bytesize)))



    def send_commands(self, commands):

        for command in commands:
            with serial.Serial(
                        port='/dev/ttyUSB1',
                        baudrate = self.baudrate,
                        parity=self.parity,
                        stopbits=self.stopbits,
                        bytesize=self.bytesize,
                        timeout=1
                    ) as ser:
   
                    s = ser.write("{}{}{}".format(command,LF,CR).encode('ascii'))
                    r = ser.read(100) # read up to one hundred bytes

                    print(r.decode("ascii"))


if __name__ == "__main__":
    rdstest = RdsTest()

    rdstest.send_commands(sys.argv[1:])
