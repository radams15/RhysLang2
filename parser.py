import ast
import sys

class Parser:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output_fun = sys.stdout.write#print

    def parse_equation(self, equation: str):
        return equation

    def parse(self, tokens: dict):
        for line, token in tokens.items():
            if ast.Object in type(token).__mro__: # .mro gets all parent classes in a list
                self.variables[token.name] = token

            if type(token) == ast.Printf:
                if token.args in self.variables:
                    self.output_fun(self.variables[token.args].value)

                elif token.args[:-2] in self.functions:
                    pass

                else:
                    self.output_fun(self.parse_equation(token.args))