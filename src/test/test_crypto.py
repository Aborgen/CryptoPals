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
    expected = bytes.fromhex("083765283065352a282463312e63212e6331292665352636356d65152b20613720323765352b2435632724223132632a343765202f29612c31292637613720323736")

    result = repeatingXOR(a, key)
    self.assertEqual(result, expected)

  def test_4_repeating_XOR_with_key_that_is_not_multiple(self):
    # Length of 66
    a = 'It is time to do the test. The test that beats out all other tests'
    key = 'TRUE'
    assert(len(a) % len(key) != 0)
    expected = bytes.fromhex('1d26752c2772212c393775313b72312a74263d2074263036207c75113c37753131212165203a3431743030242021752a21267524383e752a203a3037742630362021')

    result = repeatingXOR(a, key)
    self.assertEqual(result, expected)
