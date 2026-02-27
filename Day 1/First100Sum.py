def findSum ():
    answer = 0
    for idx in range (1,101,1):
        answer += idx
    return answer

print ("Sum of first 100 numbers:", findSum())