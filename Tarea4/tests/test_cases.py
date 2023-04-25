from src.clock_factory import *
from src.display_number import *
from src.clock_display import *
from unittest import TestCase


class Tests(TestCase):
    def test_display(self):
        result = []
        invariant_result = []
        excepted_invariant = True
        display = NumberDisplay(0, 24)
        display2 = display.clone()
        result.append(display.str())
        for i in range(100):
            display.increase()
            display2.increase()
            invariant_result = display.invariant()
            result.append(display.str())

            self.assertEqual(invariant_result, excepted_invariant)

        display.reset()
        display2.reset()

        excepted_result = ['00', '01', '02', '03', '04',
                           '05', '06', '07', '08', '09',
                           '10', '11', '12', '13', '14',
                           '15', '16', '17', '18', '19',
                           '20', '21', '22', '23', '00',
                           '01', '02', '03', '04', '05',
                           '06', '07', '08', '09', '10',
                           '11', '12', '13', '14', '15',
                           '16', '17', '18', '19', '20',
                           '21', '22', '23', '00', '01',
                           '02', '03', '04', '05', '06',
                           '07', '08', '09', '10', '11',
                           '12', '13', '14', '15', '16',
                           '17', '18', '19', '20', '21',
                           '22', '23', '00', '01', '02',
                           '03', '04', '05', '06', '07',
                           '08', '09', '10', '11', '12',
                           '13', '14', '15', '16', '17',
                           '18', '19', '20', '21', '22',
                           '23', '00', '01', '02', '03', '04']

        self.assertEqual(result, excepted_result)

    def test_clock(self):
        ## Parte 1
        result = []
        invariant_result = []
        clock = ClockDisplay([24, 60])
        result.append(clock.str())
        invariant_result.append(clock.invariant())
        clock2 = clock.clone()
        for i in range(100):
            clock.increment()
            """ print(f"incrementando clock en iteración {i}") """
            clock2.increment()

            result.append(clock.str())
            invariant_result.append(clock.invariant())


        excepted_result = list(map(lambda x: f"{x//60:02d}:{x%60:02d}", range(101)))

        excepted_invariant = [True for i in range(101)]

        self.assertEqual(result, excepted_result)
        self.assertEqual(invariant_result, excepted_invariant)

        ## Parte 2
        result = []
        invariant_result = []
        clock = ClockDisplay([24, 60])
        clock.numbers[0].value=23
        clock.numbers[1].value=59
        clock.increment()
        result.append(clock.str())
        invariant_result.append(clock.invariant())

        excepted_result = ["00:00"]
        excepted_invariant = [True]

        self.assertEqual(result, excepted_result)
        self.assertEqual(invariant_result, excepted_invariant)

    def test_factory(self):
        factory = ClockFactory()
        result = []
        invariant_result = []
        clock = factory.create("hh:mm")
        result.append(clock.str())
        invariant_result.append(clock.invariant())
        clock2 = factory.create("hh:mm:ss")
        clock3 = factory.create("hh:mm:ss:mmmm")
        for i in range(100):
            clock.increment()
            clock2.increment()
            clock3.increment()
            result.append(clock.str())
            invariant_result.append(clock.invariant())
        
        excepted_result = list(map(lambda x: f"{x//60:02d}:{x%60:02d}", range(101)))

        excepted_invariant = [True for i in range(101)]

        self.assertEqual(result, excepted_result)
        self.assertEqual(invariant_result, excepted_invariant)
