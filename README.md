Run: python3 rdstest.py '<rds_command>'

Example:
pi@raspberrypi:~/dev/pirards $ python3 rdstest.py 'PS=to panga'
Initializing RDS comms:
BAUD RATE=19200 PARITY=N STOPBITS=1.5 BYTESIZE=8
b'P=t pnga\r\n+\r\n\r\n'
pi@raspberrypi:~/dev/pirards $ python3 rdstest.py 'PS'
Initializing RDS comms:
BAUD RATE=19200 PARITY=N STOPBITS=1.5 BYTESIZE=8
b'PS\r\nto panga\r\n+\r\n\r\n'

