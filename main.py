import lexer
import parser

if __name__ == '__main__':
    file_data = open("textProgram.rl", "r").read()
    #print(fileData)

    lex = lexer.Lexer()

    tokens = lex.lex(file_data)

    for line, token in tokens.items():
        print(token)

    #parse = parser.Parser()


