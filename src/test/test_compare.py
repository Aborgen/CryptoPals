import unittest as ut
import initTest
from modules.utils.compare import hammingDistance, isBytes, isHex

class check_types(ut.TestCase):
  def test_0_check_hex_with_valid_hex(self):
    hexString = 'deadbeef'
    assert isHex(hexString)
  
  def test_1_check_hex_with_invalid_hex(self):
    hexStrings = ['eval(evil())', '5', 'Lovely beef', '!@#$%^&*()_-+=']
    for hexString in hexStrings:
      assert not isHex(hexString)

  def test_2_check_bytes_with_valid_bytes(self):
    b = bytes.fromhex('deadbeef')
    assert isBytes(b)
  
  def test_3_check_bytes_with_invalid_bytes(self):
    b = 'deadbeef'
    assert not isBytes(bytes)

def compute_hamming_distance():
  a = 'this is a test'
  b = 'wokka wokka!!!'
  expected = 37
  result = hammingDistance(a, b)
  assert result == expected
