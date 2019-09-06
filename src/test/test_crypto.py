import unittest as ut
import initTest
from modules.crypto.crypto import fixedXOR, repeatingXOR 

class encrypt_with_XOR(ut.TestCase):
  def test_0_fixed_length_XOR_with_equal_length_buffers(self):
    a = '5468697320697320612074657374206d6573736167652e'
    b = '4e61727920626565662e20556e6c65737320646561642e'
    expected = bytes.fromhex('1a091b0a000b1645070e54301d18451e16531704060100')

    result = fixedXOR(a, b)
    self.assertEqual(result, expected)

  def test_1_fixed_length_XOR_with_unequal_length_buffers_should_truncate(self):
    a = '5468697320697320612074657374206d6573736167652e'
    b = '4e61727920626565662e20556e6c65737320646561642e'
    excess = 'deadbeef' * 5
    expected = bytes.fromhex('1a091b0a000b1645070e54301d18451e16531704060100')

    result0 = fixedXOR(a + excess, b)
    result1 = fixedXOR(a, b + excess)
    self.assertEqual(result0, expected)
    self.assertEqual(result1, expected)

  def test_2_single_byte_repeating_XOR(self):
    a = 'deadbeef'
    key = 'G'
    expected = b'\x99\xea\xf9\xa8'
    
    result = repeatingXOR(a, key)
    self.assertEqual(result, expected)

  def test_3_repeating_XOR_with_key_that_is_multiple(self):
    # Length of 66
    a = 'It is time to do the test. The test that beats out all other tests'
    key = 'ACE'
    assert(len(a) % len(key) == 0)
    expected = b'\xe5\x9e\xee\xc5\x99\xee' \
               b'\xd8\x83\xa3\xc9\xca\xba' \
               b'\xc3\xca\xaa\xc3\xca\xba' \
               b'\xc4\x8f\xee\xd8\x8f\xbd' \
               b'\xd8\xc4\xee\xf8\x82\xab' \
               b'\x8c\x9e\xab\xdf\x9e\xee' \
               b'\xd8\x82\xaf\xd8\xca\xac' \
               b'\xc9\x8b\xba\xdf\xca\xa1' \
               b'\xd9\x9e\xee\xcd\x86\xa2' \
               b'\x8c\x85\xba\xc4\x8f\xbc' \
               b'\x8c\x9e\xab\xdf\x9e\xbd'

    result = repeatingXOR(a, key)
    self.assertEqual(result, expected)

  def test_4_repeating_XOR_with_key_that_is_not_multiple(self):
    # Length of 66
    a = 'It is time to do the test. The test that beats out all other tests'
    key = 'BEEF'
    assert(len(a) % len(key) != 0)
    expected = b'\xf7\x9b\x9e\x86\xcd\xcf' \
               b'\xca\x86\xd3\x8a\x9e\x9b' \
               b'\xd1\xcf\xda\x80\x9e\x9b' \
               b'\xd6\x8a\x9e\x9b\xdb\x9c' \
               b'\xca\xc1\x9e\xbb\xd6\x8a' \
               b'\x9e\x9b\xdb\x9c\xca\xcf' \
               b'\xca\x87\xdf\x9b\x9e\x8d' \
               b'\xdb\x8e\xca\x9c\x9e\x80' \
               b'\xcb\x9b\x9e\x8e\xd2\x83' \
               b'\x9e\x80\xca\x87\xdb\x9d' \
               b'\x9e\x9b\xdb\x9c\xca\x9c'
   
    result = repeatingXOR(a, key)
    self.assertEqual(result, expected)
