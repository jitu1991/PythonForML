import random
import sys
import os
import re
import pickle
from urllib.request import urlopen
import zipfile
import bz2

'''
#Challenge 0
#print(2**38)
#print(pow(2,38))

k = 1;
for i in range(38):
    k *= 2
#print(k)


#Challenge 1
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
a = chr(100)
b = ord('a')
#print(a)
#print(b)

result = ''
for c in string:
    if c > 'a' and c < 'z':
        result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a')) 
    else:
        result +=c

#print(result)

table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
#print(string.translate(table))

#Challenge 2
data = open('level2.txt').read()
#print(data)
text = "".join(re.findall("[A-Za-z]", data))
#print(text)

#Challenge 3
data = open('level3.txt').read()
#need to find the pattern AAAbCCC
pattern = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"
#print("".join(re.findall(pattern, data)))

#Challenge 4
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
pattern = re.compile("and the next nothing is (\d+)")

while True:
    content = urlopen(uri%num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    #print(match)
    if match == None:
        break
    num = match.group(1)

#Challenge 5
data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print(data)
for line in data:
    print("".join([k * v for k, v in line]))

#Challenge 6
f = zipfile.ZipFile("C:/Users/jitender.kumar/Downloads/channel.zip")
num = '90052'
comments = []
while True:
    content = f.read(num+".txt").decode("utf-8")
    comments.append(f.getinfo(num+".txt").comment.decode('utf-8'))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    #print(match)
    if match == None:
        break
    num = match.group(1)
print("".join(comments))

#Challenge 7 - Image Processing library

#Challenge 8 - zip in python
#b' - convert string to bytes
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un))
print(bz2.decompress(pw))

#Challenge 9 - Image Processing Library

first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399]

second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136]


#Challenge 10 - Look and say sequence
# clicking on image - a = [1, 11, 21, 1211, 111221, 

#Solution 1
a = '1'
b = ''
for i in range(0,30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]:
            k += 1
        b += str(k-j) + a[j]
        j = k
    print(b)
    a = b
    b = ''
print(len(a))

#Solution 2

re.findall(r"(\d)(\1*)", "111221")
'''

