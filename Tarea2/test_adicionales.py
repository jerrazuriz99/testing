import unittest
from rules import *
from rewriter import *

"""
Template para los tests de las reglas y transformaciones adicionales propuestos por usted.
IMPORTANTE: 
    - Deben existir al menos 5 tests, uno por cada regla/transformador implementado.
    - Los codigos a ser analizados usados en los tests deben ser diferentes.
    - Los tests adicionales deben ser diferentes a los del archivo tests-tarea.py
    - Si usted implemento la tarea en un nuevo archivo dentro del folder rules o rewriter
    no olvide modificar el __init__.py de rules y rewriter para importar los archivos necesarios para su tarea.
    Caso contrario importe lo necesario en este archivo.
"""

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_long_variable_name
        Codigo a ser analizado: extra-test-code/longVariableName.py
        Descripcion: Test para evaluar LongVariableNameRule considerando los siguientes escenarios:
        - Linea 6: Uso de variable de nombre largo : longnameforahouse
        - Linea 7: Uso de variable de nombre largo : longnameforaperson
        - Linea 11: Uso de variable de instancia de nombre largo: longnameforahouse
        - Linea 12: Uso de variable de instancia de nombre largo: longnameforaperson
        - Linea 11 y 12: Uso de variables de nombre corto (<= 15)
        
        Resultado esperado:
        [Warning('VariableLongName', 6, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 7, 'variable longnameforaperson has a long name'),
        Warning('VariableLongName', 11, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 11, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 12, 'variable longnameforaperson has a long name'),
        Warning('VariableLongName', 12, 'variable longnameforaperson has a long name'),
        ]
    """

    def test_long_variable_name(self):
        tree = self.get_ast_from_file('extra-test-code/longVariableName.py')

        longNameRule = LongVariableNameRule()
        result = longNameRule.analyze(tree)

        expectedWarnings = [
        Warning('VariableLongName', 6, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 7, 'variable longnameforaperson has a long name'),
        Warning('VariableLongName', 11, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 11, 'variable longnameforahouse has a long name'),
        Warning('VariableLongName', 12, 'variable longnameforaperson has a long name'),
        Warning('VariableLongName', 12, 'variable longnameforaperson has a long name'),
        ]

        """ for i in range(len(result)):
            print(f"Expected: {expectedWarnings[i].name} - Result: {result[i].name}") """

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_unused_argument
        Codigo a ser analizado: extra-test-code/unusedArgument.py
        Descripcion: Test para evaluar UnusedArgumentRule considerando los siguientes escenarios:
        - Linea 1: Argumento x no usado
        - Linea 6: Argumento d no usado
        - Linea 16: Argumento ps no usado
        - Linea 24: Argumento ts no usado
        
        Resultado esperado:
        [Warning('UnusedArgument', 1, 'argument x is not used'),
        Warning('UnusedArgument', 6, 'argument d is not used'),
        Warning('UnusedArgument', 16, 'argument ps is not used'),
        Warning('UnusedArgument', 24, 'argument ts is not used'),
        ]
    """

    def test_unused_argument(self):
        tree = self.get_ast_from_file('extra-test-code/unusedArgument.py')

        unusedArgRule = UnusedArgumentRule()
        result = unusedArgRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
        Warning('UnusedArgument', 1, 'argument x is not used'),
        Warning('UnusedArgument', 6, 'argument d is not used'),
        Warning('UnusedArgument', 16, 'argument ps is not used'),
        Warning('UnusedArgument', 24, 'argument ts is not used'),
        ]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_super_init_not_called
        Codigo a ser analizado: extra-test-code/superInitNotCalled.py
        Descripcion: Test para evaluar SuperInitNotCalledRule considerando los siguientes escenarios:
        - Linea 10: Subclase Football no llama a super().__init__()
        - Linea 25: Subclase Futsal no llama a super().__init__()

        Resultado esperado:
        [Warning('SuperInitNotCalled', 10, 'subclass Football does not call to super().__init__()'),
        Warning('SuperInitNotCalled', 25, 'subclass Futsal does not call to super().__init__()'),
        ]
    """

    def test_super_init_not_called(self):
        tree = self.get_ast_from_file('extra-test-code/superInitNotCalled.py')

        superInitRule = SuperInitNotCalledRule()
        result = superInitRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
        Warning('SuperInitNotCalled', 10, 'subclass Football does not call to super().__init__()'),
        Warning('SuperInitNotCalled', 25, 'subclass Futsal does not call to super().__init__()'),
        ]

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_minus_equal_rewriter
        Codigo a ser analizado: extra-test-code/minusEquals.py
        Descripcion: Test para evaluar transformador MinusEqualsRewriterCommand considerando los siguientes escenarios:
        - Linea 6: a -= 3
        - Linea 7: c -= b
        - Linea 8: d -= c
        - Linea 12: g -= f
        - Linea 13: f -= e
        - Linea 14: e -= g
        - Linea 18: k -= j
        - Linea 19: j -= i
        - Linea 20: i -= h
        - Linea 21: h -= k

        Resultado esperado: extra-test-code/expectedMinusEquals.py
    """

    def test_minus_equal_rewriter(self):
        tree = self.get_ast_from_file('extra-test-code/minusEquals.py')

        command = MinusEqualsRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedMinusEquals.py')
        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_simplified_if
        Codigo a ser analizado: extra-test-code/simplifiedIf.py
        Descripcion: Test para evaluar SimplifiedIfRewriterCommand considerando los siguientes escenarios:
        - Linea 4: Uso de la expresion if cuando puede ser reemplazada por el if.test
        - Linea 9: Uso de la expresion if cuando puede ser reemplazada por el not if.test
        - Linea 15: Uso de la expresion if cuando puede ser reemplazada por el not if.test
        
        Resultado esperado: extra-test-code/expectedSimplifiedIf.py
    """

    def test_simplified_if(self):
        tree = self.get_ast_from_file('extra-test-code/simplifiedIf.py')

        command = SimplifiedIfRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedSimplifiedIf.py')
        
        self.assertEqual(dump(tree), dump(expectedCode))

if __name__ == '__main__':
    unittest.main()
