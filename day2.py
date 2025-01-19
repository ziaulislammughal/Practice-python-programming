#  LOOPS .
# FOR loop 
 # WHILE LOOP 

for i in range(1,11,3):  #index start from 0 to 9            range(start,stop,step)
 print(i)          #output 0,1,2,3,4,5,6,7,8,9
    
    
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in fruits:
     print(i)       # output apple, banana, cherry, date, elderberry


# while loop

count=1 
while count<1000:
    print(count)
    count += 1      # increment count by 1 each time
    count = count**2   # increment count by 1 each time
    
    
# break and continue statement . 
for i in range(10):
    if i == 5:
        continue  # stop the loop when i equals 5
    print(i)  #output 0,1,2,3,4, we use continue os iteration is print 5 and move on ,6,7,8,9
    
    
for i in range(10):
    if i == 5:
        break  # stop the loop when i equals 5
    print(i) #output 0,1,2,3,4
    
    
    