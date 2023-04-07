from ast import *
import os
from profiler import Profiler


class ClassInstrumentor(NodeTransformer):

    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse(
            "from classInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)

    def visit_ClassDef(self, node: ClassDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        # recorremos los metodos de la clase
        for method in transformedNode.body:
            if isinstance(method, FunctionDef):
                # Inyectamos codigo para llamar al profiler en la primera linea de la definicion de una funcion
                argList = list(map(lambda x: x.arg, method.args.args))
                injectedCode = parse('ClassProfiler.record(\'' +
                                     method.name + '\', ' + str(method.lineno) + ', \'' + transformedNode.name + '\')')
                if isinstance(method.body, list):
                    method.body.insert(0, injectedCode.body[0])
                else:
                    method.body = [injectedCode.body[0], node.body]

                fix_missing_locations(transformedNode)

        return transformedNode

    def visit_FunctionDef(self, node: FunctionDef):
        self.function_name = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        return transformedNode

    def visit_Call(self, node: Call):
        transformedNode = NodeTransformer.generic_visit(self, node)
        print("=======================================")
        print("transformedNode: " + unparse(transformedNode))
        if isinstance(transformedNode.func, Attribute) and isinstance(transformedNode.func.value, Name):
            # Encontrar la función que se llama
            function_name = transformedNode.func.attr
            print("function_name: " + function_name)
            # Encontrar el nombre de la clase que se llama
            class_name = transformedNode.func.value.id
            print("class_name: " + class_name)
            # Encontrar el número de línea de la llamada
            line_number = transformedNode.lineno
            print("line_number: " + str(line_number))
            # Encontrar el nombre del método que llama a la función
            method_name = self.function_name
            print("method_name: " + method_name)

            injectedCode = parse('ClassProfiler.recordUsed(\'' +
                                 method_name + '\', ' + str(line_number) + ', \'' + class_name + '\', \'' + function_name + '\')')
            print("injectedCode: " + unparse(injectedCode))
            transformedNode = injectedCode.body[0]
            fix_missing_locations(transformedNode)
        # else if es un rectangle = Rectangle(2, 3), functionName = __init__
        # else if es un rectangle1 != rectangle2, functionName = __eq__
        elif isinstance(transformedNode.func, Name):
            # Encontrar el nombre de la clase que se llama
            class_name = transformedNode.func.id
            print("class_name: " + class_name)
            # Encontrar el número de línea de la llamada
            line_number = transformedNode.lineno
            print("line_number: " + str(line_number))
            # Encontrar el nombre del método que llama a la función
            method_name = self.function_name
            print("method_name: " + method_name)
            # Encontrar el nombre de la función que se llama
            function_name = "__init__" if class_name == method_name else "__eq__"
            print("function_name: " + function_name)

            injectedCode = parse('ClassProfiler.recordUsed(\'' +
                                 method_name + '\', ' + str(line_number) + ', \'' + class_name + '\', \'' + function_name + '\')')
            print("injectedCode: " + unparse(injectedCode))
            transformedNode = injectedCode.body[0]
            fix_missing_locations(transformedNode)


class ClassProfiler(Profiler):

    @ classmethod
    def record(cls, methodName, lineNumber, className):
        cls.getInstance().ins_record(methodName, lineNumber, className)

    def recordUsed(self, methodName, lineNumber, className, function):
        self.getInstance().ins_record(methodName, lineNumber, className, function)

    # Metodos de instancia
    def __init__(self):
        self.methods_called = []
        self.methods_used = []
        self.function_name = None

    def ins_record(self, methodName, lineNumber, className):
        if (methodName, lineNumber, className) not in self.methods_called:
            self.methods_called.append((methodName, lineNumber, className))

    def report_executed_methods(self):
        print("-- Executed methods --")
        self.methods_called.sort(key=lambda t: t[1])
        for (fun, lineNumber, className) in self.methods_called:
            print("Method " + fun + " in class " + className +
                  " at line " + str(lineNumber))
        return self.methods_called

    def report_executed_by(self, function_name):
        # Este metodo recibe el nombre de una funci´on ejecutada (no pertenece a una clase) y retorna una lista de tuplas que representan los m´etodos que fueron llamados por esa funci´on.
        # La lista retornada esta ordenada descendentemente en base al segundo elemento de cada tupla (t[1]), donde cada tupla sigue el formato:
        # (<method-name>,<codeline-methodDef>,
        # <method-class>)
        print("-- Executed by --")
        print("function_name: " + function_name)


def instrument(ast):
    visitor = ClassInstrumentor()
    return fix_missing_locations(visitor.visit(ast))
