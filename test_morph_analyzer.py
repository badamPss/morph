import unittest
from morph_analyzer import analyze_word

class TestMorphAnalyzer(unittest.TestCase):
    def test_begal(self):
        result = analyze_word("бежал")
        self.assertEqual(result["pos"], "VERB")
        self.assertIn("прошедшее время", result["grammar"])
        self.assertIn("глагол", result["pos_ru"])

    def test_dom(self):
        result = analyze_word("дом")
        self.assertEqual(result["pos"], "NOUN")
        self.assertIn("существительное", result["pos_ru"])
        self.assertIn("неодушевлённое", result["grammar"])

    def test_krasivaya(self):
        result = analyze_word("красивая")
        self.assertEqual(result["pos"], "ADJF")
        self.assertIn("прилагательное (полное)", result["pos_ru"])
        self.assertIn("женский род", result["grammar"])
        self.assertIn("единственное число", result["grammar"])
        self.assertIn("именительный падеж", result["grammar"])

    def test_bystro(self):
        result = analyze_word("быстро")
        self.assertEqual(result["pos"], "ADVB")
        self.assertIn("наречие", result["pos_ru"])

    def test_ya(self):
        result = analyze_word("я")
        self.assertEqual(result["pos"], "NPRO")
        self.assertIn("местоимение", result["pos_ru"])
        self.assertIn("1 лицо", result["grammar"])
        self.assertIn("единственное число", result["grammar"])

    def test_pyat(self):
        result = analyze_word("пять")
        self.assertEqual(result["pos"], "NUMR")
        self.assertIn("числительное", result["pos_ru"])

    def test_begat(self):
        result = analyze_word("бегать")
        self.assertEqual(result["pos"], "INFN")
        self.assertIn("инфинитив", result["pos_ru"])
        self.assertIn("несовершенный вид", result["grammar"])

    def test_begushchiy(self):
        result = analyze_word("бегущий")
        self.assertEqual(result["pos"], "PRTF")
        self.assertIn("причастие (полное)", result["pos_ru"])
        self.assertIn("настоящее время", result["grammar"])

    def test_empty(self):
        result = analyze_word("")
        self.assertIsInstance(result, dict)  # Просто тест на структуру

if __name__ == '__main__':
    unittest.main()