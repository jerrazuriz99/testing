from .rewriter import *


class SimplifiedIfTransformer(NodeTransformer):

    def visit_Return(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node.value, IfExp):
            test = node.value.test
            """ print(dump(test)) """
            if_true = node.value.body
            if_false = node.value.orelse
            """ print(f"if_true: {if_true} and if_false: {if_false}") """
            if_true_value = if_true.value
            if_false_value = if_false.value if if_false else None
            """ print(f"if_true_value: {if_true_value} and if_false_value: {if_false_value} left: {left.id} ops {ops[0]} comparators: {comparators[0].id}") """
            if if_true_value == True and if_false_value == False:
                """ print("Check case 1") """
                node.value = test
            elif if_true_value == False and if_false_value == True:
                # Crea el nodo ast.UnaryOp con el operador "not"
                not_node = UnaryOp(op=Not(), operand=test)
                """ print("Check case 2") """
                node.value = not_node
            else:
                node.value = node.value

        return node

class SimplifiedIfRewriterCommand(RewriterCommand):

      def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree