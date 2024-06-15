class token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
        


class lex:
    def __init__(self, source):
        #adds 
        self.source = source + '\n' #adds newline to the end of the source code
        self.curChar = '' #curr character
        self.curPos = -1 #curr position
        self.nextChar() #next character
    
    #processes the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]
    
    #return lookahead character
    def peek(self):
        pass
    
    #Invalid token found, print error message and exit
    def abort(self, message):
        pass
    
    #skip whitespace
    def skipWhitespace(self):
        pass
    
    #skip comments
    def skipComment(self):
        pass
    
    #return token
    def getToken(self):
        #checks for each token
        if self.curChar == '+':
            pass
        elif self.curChar == '-':
            pass
        elif self.curChar == '*':
            pass
        elif self.curChar == '/':
            pass
        elif self.curChar == '\0':
            pass
        elif self.curChar == '\n':
            pass
        else:
            pass
        
        self.nextChar()