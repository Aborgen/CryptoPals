import unittest as ut
import initTest
from modules.utils.convert import hex2b64

class convert_from_hex_to_base64(ut.TestCase):
  def test_0_valid_input(self):
    value = ("49276d206b696c6c696e6720796f757220627261696e206c"
             "696b65206120706f69736f6e6f7573206d757368726f6f6d")
    expected = ("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBs"
                "aWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
    result = hex2b64(value)
    self.assertEqual(result, expected.encode())

  def test_1_invalid_input(self):
    values = {
      "This is not hex!",
      "48454c4c4g",
      "5",
      "{%$@@!^}"
    }

    for value in values:
      self.assertRaises(ValueError, hex2b64, value)
