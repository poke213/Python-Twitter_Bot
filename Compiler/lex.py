import enum
import sys

#class for Token
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
        
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in tokenType:
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None

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
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]
    
    #Invalid token found, print error message and exit
    def abort(self, message):
        sys.exit("Lexing error: " + message)
    
    #skip whitespace
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()
    
    #skip comments
    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()
    
    #return token
    def getToken(self):
        
        self.skipWhitespace()
        self.skipComment()
        token = None
        
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

        elif self.curChar == '=':
            # Check whether this token is = or ==
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, tokenType.EQEQ)
            else:
                token = Token(self.curChar, tokenType.EQ)
        elif self.curChar == '>':
            # Check whether this is token is > or >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, tokenType.GTEQ)
            else:
                token = Token(self.curChar, tokenType.GT)
        elif self.curChar == '<':
                # Check whether this is token is < or <=
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, tokenType.LTEQ)
                else:
                    token = Token(self.curChar, tokenType.LT)
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, tokenType.NOTEQ)
            else:
                peek = self.peek()
                if peek is None:
                    peek = "EOF"
                self.abort("Expected !=, got !" + peek)
        
        #checking for digits
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Illegal character in number: " + self.peek())
                while self.peek().isdigit():
                    self.nextChar()
            tokText = self.source[startPos : self.curPos + 1]
            token = Token(tokText, tokenType.NUMBER)
            
        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
                
            tokText = self.source[startPos : self.curPos + 1]
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None:
                token = Token(tokText, tokenType.INDENT)
            else:
                token = Token(tokText, keyword)
        else:
            self.abort("Unknown token: " + self.curChar)
        
        self.nextChar()
        return token