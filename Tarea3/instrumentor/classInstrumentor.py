from ast import *
import os
from profiler import Profiler


class ClassInstrumentor(NodeTransformer):

    def __init__(self):
        self.current_class = None

    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse(
            "from classInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)

        return transformedNode

    def visit_ClassDef(self, node: ClassDef):
        self.current_class = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        # recorremos los metodos de la clase
        for method in transformedNode.body:
            if isinstance(method, FunctionDef):
                # Inyectamos codigo para llamar al profiler en la primera linea de la definicion de una funcion
                function = 'record'
                injectedCode = parse('ClassProfiler.record(\'' +
                                     method.name + '\', ' +
                                     str(method.lineno) + ', \'' +
                                     transformedNode.name + '\', \'' + function + '\')')
                if isinstance(method.body, list):
                    method.body.insert(0, injectedCode.body[0])
                else:
                    method.body = [injectedCode.body[0], node.body]

                fix_missing_locations(transformedNode)

        return transformedNode

    # Recorrer las funciones y buscar rectangle1 = Rectangle(2, 3), assert rectangle1 != rectangle2, 'Different rectangles' o assert rectangle.get_area() == 6, 'Incorrect area'
    def visit_FunctionDef(self, node: FunctionDef):
        self.function_name = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        return transformedNode

    def visit_Assign(self, node: Assign):
        transformedNode = NodeTransformer.generic_visit(self, node)
        # Si es una asignacion de una clase, inyectamos codigo para llamar al profiler
        if isinstance(transformedNode.value, Call):
            if isinstance(transformedNode.value.func, Name):
                if transformedNode.value.func.id in self.current_class:
                    method = '__init__'
                    injectedCode = parse('ClassProfiler.record(\'' + method + '\', ' + str(
                        transformedNode.lineno) + ', \'' + self.current_class + '\', \'' + self.function_name + '\')')
                    # insert despues de transformNode con salto de linea
                    new_body = [transformedNode,
                                injectedCode.body[0]]
                    transformedNode = parse(
                        f'{unparse(new_body[0])}\n{unparse(new_body[1])}')
                    fix_missing_locations(transformedNode)
        return transformedNode

    def visit_Assert(self, node: Assert):
        transformedNode = NodeTransformer.generic_visit(self, node)
        # Si es una comparacion de una clase, inyectamos codigo para llamar al profiler
        if isinstance(transformedNode.test.left, Name):
            method = '__eq__'
            injectedCode = parse('ClassProfiler.record(\'' +
                                 method + '\', ' + str(transformedNode.lineno) + ', \'' + self.current_class + '\', \'' + self.function_name + '\')')
            # insert despues de transformNode con salto de linea
            new_body = [transformedNode,
                        injectedCode.body[0]]
            transformedNode = parse(
                f'{unparse(new_body[0])}\n{unparse(new_body[1])}')
            # print(unparse(transformedNode))
            fix_missing_locations(transformedNode)
        elif isinstance(transformedNode.test.left, Call):
            method = transformedNode.test.left.func.attr
            injectedCode = parse('ClassProfiler.record(\'' +
                                 method + '\', ' + str(transformedNode.lineno) + ', \'' + self.current_class + '\', \'' + self.function_name + '\')')
            # insert despues de transformNode con salto de linea
            new_body = [transformedNode,
                        injectedCode.body[0]]
            transformedNode = parse(
                f'{unparse(new_body[0])}\n{unparse(new_body[1])}')
            # print(unparse(transformedNode))
            fix_missing_locations(transformedNode)
        return transformedNode


class ClassProfiler(Profiler):

    @ classmethod
    def record(cls, methodName, lineNumber, className, function):
        cls.getInstance().ins_record(methodName, lineNumber, className, function)

    # Metodos de instancia
    def __init__(self):
        self.methods_called = []
        self.methods_used = []
        self.function_name = None

    def ins_record(self, methodName, lineNumber, className, function):
        if function == 'record':
            if (methodName, lineNumber, className) not in self.methods_called:
                self.methods_called.append((methodName, lineNumber, className))
        else:
            if (methodName, lineNumber, className, function) not in self.methods_used:
                self.methods_used.append(
                    (methodName, lineNumber, className, function))

    def report_executed_methods(self):
        print("-- Executed methods --")
        self.methods_called.sort(key=lambda t: t[1])
        for (fun, lineNumber, className) in self.methods_called:
            print("Method " + fun + " in class " + className +
                  " at line " + str(lineNumber))
        return self.methods_called

    def report_executed_by(self, function_name):
        print("-- Executed by --")
        methods = []

        for (fun, lineNumber, className, function) in self.methods_used:
            if function == function_name:
                print("Method " + fun + " in class " + className +
                      " at line " + str(lineNumber))
                # buscar en self.methods_called cual es la linea de ejecucion de ese metodo
                for (fun2, lineNumber2, className2) in self.methods_called:
                    if fun == fun2 and className == className2:
                        print("Executed at line " + str(lineNumber2))
                        methods.append((fun, lineNumber2, className))
                # eliminar elementos repetidos
        methods = list(dict.fromkeys(methods))
        return methods


def instrument(ast):
    visitor = ClassInstrumentor()
    return fix_missing_locations(visitor.visit(ast))
