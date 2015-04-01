import symulator
import unittest

class TestSymulator(unittest.TestCase):
   
   def setUp(self):
       self.repairRight=symulator.RepairFly(1,200)
       self.repairLeft=symulator.RepairFly(0,200)

   def test_pass(self):
       self.assertTrue(True)
   
   def test_0_is_left(self):
       self.assertEquals(self.repairRight.dict["dir"],"right")
       self.assertEquals(self.repairRight.dict["alpha"],200)

   def test_1_is_right(self):
       self.assertEquals(self.repairLeft.dict["dir"],"left")
       self.assertEquals(self.repairLeft.dict["alpha"],200)

   def test_type_int(self):
       self.assertRaises(TypeError,RepairFly.("String1","String2")
   
   
if __name__ == '__main__':
    unittest.main()   
