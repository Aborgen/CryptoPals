import unittest as ut
import initTest
from modules.utils.convert import hex2b64, hex2bytes, bytes2hex

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

class convert_from_hex_to_bytes(ut.TestCase):
  def test_0_valid_input(self):
    value = "deadbeef"
    expected = b"\xde\xad\xbe\xef"
    result = hex2bytes(value)
    self.assertEqual(result, expected)

  def test_0_invalid_input(self):
    values = {
      "This is not hex!",
      "48454c4c4g",
      "5",
      b"55",
      "{%$@@!^}"
    }

    for value in values:
      self.assertRaises(ValueError, hex2bytes, value)

class convert_from_bytes_to_hex(ut.TestCase):
  def test_0_valid_input(self):
    value = b"\xde\xad\xbe\xef"
    expected = "deadbeef"
    result = bytes2hex(value)
    self.assertEqual(result, expected)

  def test_0_invalid_input(self):
    values = {
      "DEADBEEF",
      "deadbeef",
      "48454c4c4f",
      "And I will walk 5000 miles",
      "{%$@@!^}"
    }

    for value in values:
      self.assertRaises(ValueError, bytes2hex, value)
