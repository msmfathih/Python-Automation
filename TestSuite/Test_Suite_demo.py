import unittest
from TestSuite.TestSuite1 import TestSuiteDemo1
from TestSuite.TestSuite2 import TestSuiteDemo2
from TestSuite.TestSuite3 import TestSuiteDemo3
from TestSuite.TestSuite4 import TestSuiteDemo4

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteDemo2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteDemo3)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteDemo4)



smoke_test = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
