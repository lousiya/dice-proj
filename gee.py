import random
sum=0
while(sum!=64):
    random_num=random.randrange(1,7)
    print"the value of the rolled die is",random_num
    if(sum+random_num<=64):
     sum=sum+random_num
    x=sum%8
    y=sum/8
    
    if(y%2==1):
      x=7-x
    print "sum=",sum
    print"the position of the die is (x,y)=",x,y
    print"\n"

if(sum==64):
    print "game won"



       
     
    



     
