import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

book = xlwt.Workbook()
sheet1 = book.add_sheet("ParseQuestions")

queFile = open("question.txt", "r")

id = 0
for que in queFile:
    row = sheet1.row(id)
    #print type(que.rstrip())
    row.write(0, que.decode('utf-8'))
    id = id+1

f = open("output.txt", "r")
#f = open("test.txt", "r")

id = 0
'''for line in f:
  lines1 = []
  lines2 = []
  row = sheet1.row(id)
  if(line[0] == "(" or line[0]==" "):
      lines1.append(line.rstrip())

  else:
      lines2.append(line.rstrip())

  row.write(1, lines1.decode('utf-8'))
  row.write(2, lines2.decode('utf-8'))
  id+1'''

data = f.read()
splat = data.split("\n\n")
id=0
count = 0
for number, paragraph in enumerate(splat, 1):
    row = sheet1.row(id)
    if number % 2 == 1:
        array1 = paragraph
        #print array1 ,id
        row.write(1, array1.decode('utf-8'))
    elif number % 2 == 0:
        array2 = paragraph
        #print array2, id
        row.write(2, array2.decode('utf-8'))
    if(count%2!=0):
        id = id+1
    count = count +1


book.save("parse_Question1.xlsx")