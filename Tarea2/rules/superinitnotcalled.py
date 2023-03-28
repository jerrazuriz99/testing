# Codigo del estudiante
from .rule import *
import ast


class SuperInitNotCalledVisitor(WarningNodeVisitor):

    def _init_(self):
        super()._init_()
        self.has_init_call = False

    def visit_ClassDef(self, node):
        if node.bases:
            self.has_init_call = False
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef) and stmt.name == '__init__':
                    for expr in stmt.body:
                        if isinstance(expr, ast.Expr) and isinstance(expr.value, ast.Call) and isinstance(expr.value.func, ast.Attribute) and expr.value.func.attr == '__init__' and isinstance(expr.value.func.value, ast.Call) and isinstance(expr.value.func.value.func, ast.Name) and expr.value.func.value.func.id == 'super':
                            self.has_init_call  = True
            if not self.has_init_call:
                """ print('subclass ' + node.name + ' does not call the super().__init__() in line' + str(node.lineno)) """
                self.addWarning('SuperInitNotCalled', node.lineno, 'subclass ' + node.name + ' does not call to super().__init__()')


class SuperInitNotCalledRule(Rule):

    def analyze(self, ast):
        visitor = SuperInitNotCalledVisitor()
        visitor.visit(ast)
        self.warningsList = visitor.warningsList()
        return self.warningsList
