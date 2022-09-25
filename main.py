print(sh1.cell(i,5).value)
print(t, end="")

elif i.startswith('+'):
k = list(i)
k.remove("+")
for count1 in range(0, len(k)):
    i = k[count1]
    p = i
    print(i, end="")




    elif i.startswith('05'):
        t = '966' + i
        l = list(t)
        l.pop(3)
        for count in range(0,len(l)):
            t = l[count]
            i = t
            print(t,end="")

for count in range(0, len(l)):
    t = l[count]
    i = t
    print(t, end="")

    wb = workbook()
    wb['sheet'].title = "after"
    she1 = wb.active