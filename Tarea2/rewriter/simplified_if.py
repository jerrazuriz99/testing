from .rewriter import *

# Clases que permiten transformar codigo que contiene 
#def example1(x, y): 
#    return True if x > y else False 
#por 
#def example(x, y): 
#    return x > y

# o 

#def example2(x, y): 
#    return False if x > y else True 
#por 
#def example(x, y): 
#    return not x > y

class SimplifiedIfTransformer(NodeTransformer):
    def visit_Return(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node.value, IfExp):
            if isinstance(node.value.test, Compare):
                if isinstance(node.value.test.ops[0], Gt):
                    if isinstance(node.value.test.left, Name):
                        if isinstance(node.value.test.comparators[0], Name):
                            if node.value.test.left.id == node.value.test.comparators[0].id:
                                node.value = node.value.test.left
                                print(f'node.value.test.left' + str(node.value.test.left))
        return node

class SimplifiedIfRewriterCommand(RewriterCommand):
  
      def apply(self, ast):
          # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
          new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
          return new_tree