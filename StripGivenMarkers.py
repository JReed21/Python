import re
def solution(string,markers):
    for x in markers: 
         string =  re.sub('[ \t]*[\{0}].*[^\n]*?'.format(x),r'',string)
    return string