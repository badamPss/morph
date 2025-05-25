#!/usr/bin/env python3
import unittest
import sys
from test_morph_analyzer import TestMorphAnalyzer

def run_tests():
    # Создаем тестовый набор
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMorphAnalyzer)
    
    # Запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Возвращаем код ошибки в зависимости от результата тестов
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests()) 