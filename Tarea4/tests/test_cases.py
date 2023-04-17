from src.clock_factory import *
from src.display_number import *
from src.clock_display import *
from unittest import TestCase


class Tests(TestCase):
    def test_display(self):
        display = NumberDisplay(0, 24)
        display2 = display.clone()
        for i in range(100):
            display.increase()
            print(display.str())
            print(display.invariant())

            display2.increase()
            print(display2.str())
            print(display2.invariant())

        display.reset()
        display2.reset()

    def test_clock(self):
        clock = ClockDisplay([24, 60])
        clock2 = clock.clone()
        for i in range(100):
            clock.increment()
            print(clock.str())
            print(clock.invariant())

            clock2.increment()
            print(clock2.str())
            print(clock2.invariant())
    
    def test_factory(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        clock2 = factory.create("hh:mm:ss")
        clock3 = factory.create("hh:mm:ss:mmmm")
        for i in range(100):
            clock.increment()
            print(clock.str())
            print(clock.invariant())

            clock2.increment()
            print(clock2.str())
            print(clock2.invariant())

            clock3.increment()
            print(clock3.str())
            print(clock3.invariant())