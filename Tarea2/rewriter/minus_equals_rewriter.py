from .rewriter import *

# Clases que permiten transformar codigo que contiene x = x - y. y como resultado reemplaza la expresion por x -= y.
class MinusEqualsTransformer(NodeTransformer):
    def visit_Assign(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node.value, BinOp):
            if isinstance(node.value.op, Sub):
                if isinstance(node.value.left, Name) and isinstance(node.value.right, Name):
                    if node.value.left.id == node.targets[0].id:
                        node.value = AugAssign(target=node.targets[0], op=Sub(), value=node.value.right)
        return node

class MinusEqualsRewriterCommand(RewriterCommand):

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(MinusEqualsTransformer().visit(ast))
        return new_tree
