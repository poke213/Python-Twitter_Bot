from lex import *

def main():
    source = "+- */"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token is not None and token.kind != tokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()