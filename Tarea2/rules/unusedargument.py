# Codigo del estudiante
from .rule import *
import ast


class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.args = set()

    def visit_FunctionDef(self, node: FunctionDef):
         # Recopilar los nombres de los argumentos de la función
        for arg in node.args.args:
            self.args.add(arg.arg)

        # Visitar los nodos hijos
        self.generic_visit(node)

    def visit_Name(self, node):
        # Verificar si el nombre se refiere a un argumento no utilizado
        ## ESTO NO ESTA CORREFCTO, HAY QUE VERIFICAR QUE EL NOMBRE NO SE ESTE USANDO EN EL CUERPO DE LA FUNCION
        if isinstance(node.ctx, ast.Load) and node.id in self.args:
            self.addWarning('UnusedArgument', node.lineno, 'argument ' + node.id + ' is not used')


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        self.warningsList = visitor.warningsList()
        return self.warningsList
