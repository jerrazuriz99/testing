import sys
import ast
import traceback
from stackInspector import StackInspector

""" Clase para rastrear funciones que fueron ejecutadas. Para su uso, considere:
with CoverageTracer() as coverage:
    function_to_be_traced()

coverage.report_executed_lines()
"""


class CoverageTracer(StackInspector):

    def __init__(self):
        super().__init__(None, self.traceit)
        self.executed_lines = []

    # Funcion que rastrea el codigo, contar cuantas veces se ejecuta cada linea de codigo
    def traceit(self, frame, event: str, arg):
        function_name = frame.f_code.co_name
        if event == "line":
            line = frame.f_lineno
            # Evitamos rastrearnos a nosotros
            if not self.our_frame(frame) and not self.problematic_frame(frame):
                self.executed_lines.append([function_name, line])

        return self.traceit

    def report_executed_lines(self):
        result = set()
        for line in self.executed_lines:
            result.add((line[0], line[1]))
        return sorted(result, key=lambda a: a[1])

    def report_execution_count(self):
        result = []
        for line in self.executed_lines:
            count = self.executed_lines.count(line)
            if (line[0], line[1], count) not in result:
                result.append((line[0], line[1], count))
        result = sorted(result, key=lambda a: a[1])
        return result
