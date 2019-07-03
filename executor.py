import ast
import sys

class Executor:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output_fun = sys.stdout.write#print


    def execute(self, tokens: list):
        for expression in tokens:
            if len(expression) == 3 and(expression[0].type == "VAR" and expression[1].type == "EQUALS"):
                self.variables[expression[0].value] = expression[2].value
        print(self.variables)