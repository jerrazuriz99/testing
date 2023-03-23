# Codigo del estudiante
from ast import *
from rule import *


class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        pass

    def visit_ClassDef(self, node: ClassDef):
        pass

    def visit_FunctionDef(self, node: FunctionDef):
        pass


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = NodeVisitor()
        visitor.visit(ast)
        self.warningsList = visitor.warningsList()
        return self.warningsList
