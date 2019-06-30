import re
import ast
import errors

DEFINITION = 0
DECLARATION = 1

class Lexer:
    def __init__(self):
        self.variable_pattern = re.compile(r"([a-zA-Z]+)\s*(.*)\s+=\s*(.*);")
        self.if_pattern = re.compile(r"if\s*\((.*)\)\s*{\s*([\s\S]*)\s*}")
        self.printf_pattern = re.compile(r"printf\((.*)\);")

    def _strip(self, data):
        return [[x for x in y if x is not ""] for y in data]

    def _sort_dict(self, dictionary):
        return {x:dictionary[x] for x in sorted(dictionary.keys())}

    def _find(self, pattern, data) -> dict:
        out = {}
        end = '.*'
        line = []
        for m in re.finditer(end, data):
            line.append(m.end())
        for m in re.finditer(pattern, data):
            line_num = next(i for i in range(len(line)) if line[i] > m.start(1))
            out[line_num] = m
        return out

    def lex(self, data):
        out = {}
        variables = self._find(self.variable_pattern, data)
        printfs = self._find(self.printf_pattern, data)

        if variables:
            for line, variable in variables.items():

                if variable[1] and variable[2] and variable[3]:
                    class_type = variable[1]
                    name = variable[2]
                    value = variable[3]
                else:
                    raise SyntaxError(f"Unknown Syntax On Line {line}: {variable}")

                if class_type == "string":
                    token = ast.String(name)
                    token.value = value[1:-1]
                elif class_type == "int":
                    token = ast.Integer(name)
                    token.value = value
                elif class_type == "float":
                    token = ast.Float(name)
                    token.value = value
                elif class_type == "char":
                    token = ast.Character(name)
                    token.value = value
                elif class_type == "bool":
                    token = ast.Boolean(name)
                    token.value = value
                else:
                    raise errors.UnknownTypeError(f"Unknown Type {type}")

                out[line] = token

        if printfs:
            for line, printf in printfs.items():
                args = printf[1]
                out[line] = ast.Printf(args)

        return self._sort_dict(out)
