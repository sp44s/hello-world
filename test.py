

filename = input("Enter File Name:- ")
filepath = "E:\\Philip\\source\\" + filename

count = 0
total = 0
with open(filepath) as q:
    for line in q:
        #print(line)
        if( line.startswith("X-DSPAM-Confidence:") == False):
            continue
        words = line.split()
        if len(words) == 2 :
            total += float(words[1])
            count += 1

if(count>0) :
    avg = total/count
    print("average is ", avg)
else :
    print("no average")



