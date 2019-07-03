import lexer
import executor

if __name__ == '__main__':
    file_data = open("textProgram.rl", "r").read()

    lex = lexer.lexify

    tokens = lex(file_data)

    for tok in tokens:
        print(tok)

    executor = executor.Executor()

    executor.execute(tokens)


