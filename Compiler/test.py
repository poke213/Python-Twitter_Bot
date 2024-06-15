from lex import *

def main():
    source = "LET x = 5"
    l = lex(source)
    
    while l.curChar != '\0':
        print(l.curChar)
        l.nextChar()
        
main()