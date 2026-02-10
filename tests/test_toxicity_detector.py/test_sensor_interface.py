import unittest
from toxicity_detector import detect_toxicity 

class TestToxicityDetector(unittest.TestCase):
def test_detect_toxicity(self):
  rising_data = [7, 8, 9, 10, 11]
  self.assertTrue(detect_toxicity(rising_data, thresold=10))

  non_rising_data = [7, 8, 7, 9, 8]
  self.assertFalse(detect_toxicity(rising_data, thresold=10))

if __name__ == "__main__":
  unittest.main()
