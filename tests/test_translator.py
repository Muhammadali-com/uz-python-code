import unittest
from uz_python_code import translate, translate_and_validate, supported_keywords, TranslationError

class TranslatorTests(unittest.TestCase):
    def test_keyword_translation(self): self.assertIn("if True:", translate("agar rost:\n    chiqar('ha')"))
    def test_string_preserved(self): self.assertEqual(translate('matn = "agar chiqar rost"'), 'matn = "agar chiqar rost"')
    def test_comment_preserved(self): self.assertIn("# agar chiqar", translate("# agar chiqar\nchiqar('ok')"))
    def test_function_and_return(self): self.assertIn("return son", translate_and_validate("standart kvadrat(son):\n    qaytar son * son"))
    def test_invalid_syntax_uzbek(self):
        with self.assertRaises(TranslationError) as err: translate_and_validate("agar rost\n    chiqar('x')")
        self.assertIn("sintaksis xatosi", str(err.exception).lower())
    def test_keyword_map_copy(self):
        words=supported_keywords(); words["yangi"]="new"; self.assertNotIn("yangi", supported_keywords())
    def test_non_string(self):
        with self.assertRaises(TypeError): translate(42)
    def test_loop(self): self.assertIn("for n in range", translate_and_validate("uchun n ichida range(3):\n    chiqar(n)"))

if __name__ == "__main__": unittest.main()
