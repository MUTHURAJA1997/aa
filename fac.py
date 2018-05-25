Number = int(input( "Enter the Range Number:"))
i = 0
a = 0
b= 1
l=[]
while(i < Number):
           if(i <= 1):
                      c = i
           else:
                      c = a + b
                      a = b
                      b = c
           
           l.append(c)
           i = i + 1
          
print(" ".join(str(v) for v in l))
