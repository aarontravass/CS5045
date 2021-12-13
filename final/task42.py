import random

#l=[1,2,4,6,8,10,2,11,2,8,4]
l=random.sample(range(0, 101), 100)

count=0
s=set()
for i in l:
    if(i%2==0):
        prev=len(s)
        s.add(i)
        if(prev==len(s)):
            temp_l = len(s)
            if (temp_l > 3):
                a = temp_l - 4
                t_sum = (a * (a + 1)) / 2
                t_sum += a + 1
                count += t_sum
            s.clear()
    else:
        temp_l=len(s)
        if(temp_l>3):
            a=temp_l-4
            t_sum=(a*(a+1))/2
            t_sum+=a+1
            count+=t_sum
        s.clear()

print(int(count))