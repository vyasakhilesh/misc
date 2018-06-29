#if(!True): !==not
#   pass

class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        super(ElectricCar, self).drive_car()


my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition
my_car.__init__("h", "hello", "d", 10)
my_car.display_car()

def flip_bit(number, n):
  number = number ^ (0b1 << n-1)
  return number

result = flip_bit(0b111, 2)
#print bin(result)

num  = 0b1100
mask = 0b0100
desired = num & mask
#if desired > 0:
#  print "Bit was on"

def check_bit4(input):
  mask = 0b1000
  desire = int(bin(input), 2) & 0b1000
  print type(bin(input))
  if desire > 0:
    return "on"
  else:
    return "off"

#print check_bit4(int(6))


n = [1,2,3,4]
'''print(list(map(lambda x:x**2,n)))
print(list(filter(lambda x: x>=2, n )))
print([x for x in n if x>2])
print([x**2 for x in n])
print(reduce(lambda x,y: x*y, n))'''

def remove_duplicates(n):
  p=[]
  for x in n:
    if(x not in p):
        p.append(x)
    else:
        print""
  return p

def median(n):
  p=sorted(n)
  if(len(p)%2==0):
    print(len(p))
    print(len(p)/2, (len(p)/2) - 1 )
    x = (n[len(p)/2]+n[len(p)/2-1])/2.0
  else:
    x = n[len(p)/2]

  return x

'''python comma for same line'''
my_dict = {"1":"Akhilesh","2":"Vyas"}
'''print my_dict.items()
print(median([4, 5, 6, 4]))
print(remove_duplicates([1,3,4,5,2,4,6,7,8,2,4]))'''

list=[x for x in range(51) if x%2==0]
#print list

to_21=range(1,22)
odds=to_21[::2]
#print odds

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Add arguments to the filter()
#print filter(lambda x: x if(x=="Python") else None, languages)

squares =[x**2 for x in range(1,11)]
#print filter(lambda x: (x>=30 and x<=70), squares)
#print (filter(lambda x:(x%3==0 or x%5==0),range(1,15)))

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
start,end,stride=len(garbled)+1,0, -2
message1=garbled[start:end:stride]
message=garbled[::-2]
#print message
#print message1