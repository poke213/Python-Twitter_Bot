import enum
import sys

#class for Token
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

#enum for token types
class tokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    INDENT = 2
    STRING = 3
    #keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDHWILE = 111
    #operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211


#Lexer class
class Lexer:
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
        sys.exit("Lexing error: " + message)
    
    #skip whitespace
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()
    
    #skip comments
    def skipComment(self):
        pass
    
    #return token
    def getToken(self):
        token = None
        
        self.skipWhitespace()
        
        #checks for each token
        if self.curChar == '+':
            token = Token(self.curChar, tokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, tokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, tokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, tokenType.SLASH)
        elif self.curChar == '\0':
            token = Token(self.curChar, tokenType.EOF)
        elif self.curChar == '\n':
            token = Token(self.curChar, tokenType.NEWLINE)
        else:
            self.abort("Unknown token: " + self.curChar)
        
        self.nextChar()
        return token