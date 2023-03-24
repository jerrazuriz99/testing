# Codigo del estudiante
from .rule import *
import ast


class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.function_args = dict()

    def visit_FunctionDef(self, node: FunctionDef):
         # Recopilar los nombres de los argumentos de la función
        for arg in node.args.args:
            self.function_args[arg.arg] = node.lineno

        # Visitar los nodos hijos
        self.generic_visit(node)
        for i in self.function_args:
            self.addWarning('UnusedArgument', self.function_args[i], 'argument ' + i + ' is not used')
        self.function_args = dict()

    def visit_Name(self, node):
        # Verificar si el nombre de la variable está en la lista de argumentos de la función
        # print(f"Valor a evaluar {node.id} dentro de {self.function_args}")
        if node.id in self.function_args:
            # Si el nombre de la variable está en la lista de argumentos de la función, eliminarlo de la lista
            self.function_args.pop(node.id)


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        self.warningsList = visitor.warningsList()
        return self.warningsList
