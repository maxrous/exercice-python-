name = "Alan Turing"
age = 42
profession = "mathematician"
person = [name, age, profession] 
text = "hello, my name is {}, I am {} years old and I am a {}" 
print(text) 

age_type = int

import unittest


import unittest


class TestNotebook(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name, "Alan Turing")

    def test_age(self):
        self.assertEqual(age, 42)

    def test_person(self):
        self.assertEqual(person, ["Alan Turing", 42, "mathematician"])

    def test_text(self):
        self.assertEqual(
            text,
            "Hello, my name is Alan Turing, I am 42 years old and I am a mathematician.",
        )

    def test_type(self):
        self.assertEqual(age_type, int)


unittest.main(argv=[""], verbosity=2, exit=False)
      
      



