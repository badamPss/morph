from morph_analyzer import analyze_word

def main():
    print("Введите слово (или 'stop' для выхода):")
    while True:
        word = input("> ").strip()
        if word.lower() == "stop":
            print("Выход из программы.")
            break
        if not word:
            print("Введите непустое слово.")
            continue

        result = analyze_word(word)

        print(f"Часть речи: {result['pos_ru']}")
        print("Грамматические характеристики:")
        for gram in result['grammar_ru']:
            print(f"  - {gram}")
        print("-" * 40)

if __name__ == "__main__":
    main()