'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.'''

s = 'azcbobobegghakl'  #2 bobs
s = 'auoeunbobnoeubobob,ntonethbobobo'  #5 bobs
#....01234567890123456789012345678901234567890
#..............10........20........30........40

#copy/paste code to tester after this line
seek = 'bob'
matches = 0

for i in range(0,len(s)):
    if s[i] == seek[0]:  #if any input char matches seek string
        if abs(i-len(s)) < len(seek):  #checks not closer to end of input than seek
            break
        match_maybe = True
        match = False
        seek_index = 0
        while (match_maybe):  #look ahead to see if subsequent chars match seek
            seek_index += 1
            if seek_index == len(seek):  #successful match each char of seek
                match = True
                break
            if s[i+seek_index] != seek[seek_index]: #does not match
                match_maybe = False
                break
        if match:
            matches += 1

print 'Number of times bob occurs is: ' + str(matches)
