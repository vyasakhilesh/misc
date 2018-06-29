



# replacements = {'a':'a,', 'b':'b,', 'c':'c,', 'd':'d,', 'e':'e,', 'f':'f,', 'g':'g,', 'h':'h,', 'i':'i,', 'j':'j,'}
# #replacements = {}
# with open('sequential-data.txt') as infile, open('sequential-data2.csv', 'w') as outfile:
#     for line in infile:
#         for src, target in replacements.iteritems():
#             line = line.replace(src, target)
#         print line
#             #line = line.rstrip(',')
#         line1 = line[:-3]+'\r\n'
#         outfile.write(line1)
#     infile.close()
#     outfile.close()

l = [(['abcd'], 8), (['c'], 6), (['bbd'], 7)]
l1 = (5, 6)
print len(l)
print len(l[0])
print len(l[0][0][0])