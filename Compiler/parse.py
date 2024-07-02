import sys
from lex import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    #Return true if current token matches
    def checkToken(self, kind):
        return kind == self.curToken.kind
    
    #Return true if next token matches
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
    
    #Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()
    
    #advance the current token
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
    
    def abort(self, message):
        sys.exit("Parser error. " + message)
    
    def statement(self):
        if self.checkToken(tokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()
            
            if self.checkToken(tokenType.STRING):
                self.nextToken()
            else:
                self.expression()
        self.nl()
    
    def nl(self):
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
    
    def program(self):
        print("PROGRAM")
        #program ::= statement program
        while not self.checkToken(tokenType.EOF):
            self.statement()