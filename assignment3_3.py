score=input("enter score")
s = float(score)
try:
     x=0.0<float(s)<1.0
except:
    print("error,enter a valid number")
    
if s>=0.9:	
    print("A")
elif s>=0.8:	
    print("B")
elif s>=0.7:	
    print("C")
elif s>=0.6:	
    print("D")
elif s<0.6:	
    print("F")
   
  #copied
"""  
score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)
"""
    
	
	
	