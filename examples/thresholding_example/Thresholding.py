import numpy

#A simple class to simulate a continous stream of data from the scanner.
class InputData():
    def __init__(self, fname):
        self.data = numpy.load(fname).flatten()
        self.cnt = 0

    def next(self):
        result = self.data[self.cnt]
        self.cnt += 1
        if self.cnt == len(self.data):
            self.cnt = 0
        return result

potatoe_treshold_high = 55000
potatoe_treshold_low  = 15000

background = 0
potatoe = 1
metal = 2

input_stream = InputData('potatoe.npy')
while True:
    data = input_stream.next()
    if data<0:
        print("Panic got invalid data:",data)
    if data>65536:
        print("Panic got invalid data:",data)
    result = background
    if data < potatoe_treshold_high:
        result = potatoe
    if data < potatoe_treshold_low:
        result = metal
    print data,result
