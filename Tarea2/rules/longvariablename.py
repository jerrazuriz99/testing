# Codigo del estudiante
from .rule import *
import ast


class LongVariableNameVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.variable_name = None
        self.threshold = 15

    def visit_Name(self, node):
        self.variable_name = node.id
        if len(self.variable_name) > self.threshold:
            self.addWarning('VariableLongName', node.lineno, 'variable ' + self.variable_name + ' has a long name')


class LongVariableNameRule(Rule):
        
    def analyze(self, ast):
        visitor = LongVariableNameVisitor()
        visitor.visit(ast)
        self.warningsList = visitor.warningsList()
        return self.warningsList