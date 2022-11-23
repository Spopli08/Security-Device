import unittest
import SD

class TestSD(unittest.TestCase):

    def test_initial_state(self):
        test = SD.SecurityDevice()
        self.assertEqual(test.state, 0)

    def test_unlock(self):
        # unlock code = 883371
        dev = SD.SecurityDevice()

        dev.enterval(8)
        dev.enterval(8)
        dev.enterval(3)
        dev.enterval(3)
        dev.enterval(7)
        dev.enterval(1)

        self.assertEqual(dev.state, 6)

    def test_lock(self):
        # lock code = 883374
        dev = SD.SecurityDevice()

        dev.enterval(8)
        dev.enterval(8)
        dev.enterval(3)
        dev.enterval(3)
        dev.enterval(7)
        dev.enterval(4)

        self.assertEqual(dev.state, 7)

    def test_no_input(self):
        # lock code = 883374
        dev = SD.SecurityDevice()

        dev.enterval('')

        self.assertEqual(dev.state, 0)

    def test_wrong_input(self):
        # lock code = 883374
        dev = SD.SecurityDevice()

        dev.enterval('dhfgs')
        dev.enterval('762387')
        dev.enterval('0')

        self.assertEqual(dev.state, 0)


test = TestSD()
test.test_initial_state()
test.test_unlock()
test.test_lock()
test.test_no_input()
test.test_wrong_input()