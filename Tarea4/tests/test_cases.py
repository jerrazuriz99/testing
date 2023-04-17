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
        result = []
        invariant_result = []
        clock = ClockDisplay([24, 60])
        result.append(clock.str())
        invariant_result.append(clock.invariant())
        clock2 = clock.clone()
        for i in range(100):
            clock.increment()
            clock2.increment()

            result.append(clock.str())
            invariant_result.append(clock.invariant())


        excepted_result = ['00:00', '00:01', '00:02', '00:03',
                           '00:04', '00:05', '00:06', '00:07',
                           '00:08', '00:09', '00:10', '00:11',
                           '00:12', '00:13', '00:14', '00:15',
                           '00:16', '00:17', '00:18', '00:19',
                           '00:20', '00:21', '00:22', '00:23',
                           '00:24', '00:25', '00:26', '00:27',
                           '00:28', '00:29', '00:30', '00:31',
                           '00:32', '00:33', '00:34', '00:35',
                           '00:36', '00:37', '00:38', '00:39',
                           '00:40', '00:41', '00:42', '00:43',
                           '00:44', '00:45', '00:46', '00:47',
                           '00:48', '00:49', '00:50', '00:51',
                           '00:52', '00:53', '00:54', '00:55',
                           '00:56', '00:57', '00:58', '00:59',
                           '01:00', '01:01', '01:02', '01:03',
                           '01:04', '01:05', '01:06', '01:07',
                           '01:08', '01:09', '01:10', '01:11',
                           '01:12', '01:13', '01:14', '01:15',
                           '01:16', '01:17', '01:18', '01:19',
                           '01:20', '01:21', '01:22', '01:23',
                           '01:24', '01:25', '01:26', '01:27',
                           '01:28', '01:29', '01:30', '01:31',
                           '01:32', '01:33', '01:34', '01:35',
                           '01:36', '01:37', '01:38', '01:39', '01:40']

        excepted_invariant = [True for i in range(101)]

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
        
        excepted_result = ['00:00', '00:01', '00:02', '00:03',
                           '00:04', '00:05', '00:06', '00:07',
                           '00:08', '00:09', '00:10', '00:11',
                           '00:12', '00:13', '00:14', '00:15',
                           '00:16', '00:17', '00:18', '00:19',
                           '00:20', '00:21', '00:22', '00:23',
                           '00:24', '00:25', '00:26', '00:27',
                           '00:28', '00:29', '00:30', '00:31',
                           '00:32', '00:33', '00:34', '00:35',
                           '00:36', '00:37', '00:38', '00:39',
                           '00:40', '00:41', '00:42', '00:43',
                           '00:44', '00:45', '00:46', '00:47',
                           '00:48', '00:49', '00:50', '00:51',
                           '00:52', '00:53', '00:54', '00:55',
                           '00:56', '00:57', '00:58', '00:59',
                           '01:00', '01:01', '01:02', '01:03',
                           '01:04', '01:05', '01:06', '01:07',
                           '01:08', '01:09', '01:10', '01:11',
                           '01:12', '01:13', '01:14', '01:15',
                           '01:16', '01:17', '01:18', '01:19',
                           '01:20', '01:21', '01:22', '01:23',
                           '01:24', '01:25', '01:26', '01:27',
                           '01:28', '01:29', '01:30', '01:31',
                           '01:32', '01:33', '01:34', '01:35',
                           '01:36', '01:37', '01:38', '01:39', '01:40']

        excepted_invariant = [True for i in range(101)]

        self.assertEqual(result, excepted_result)
        self.assertEqual(invariant_result, excepted_invariant)
