import pymorphy2

morph = pymorphy2.MorphAnalyzer()

GRAMMAR_TRANSLATIONS = {
    "past": "прошедшее время",
    "pres": "настоящее время",
    "futr": "будущее время",
    "indc": "изъявительное наклонение",
    "impr": "повелительное наклонение",
    "tran": "переходный",
    "intr": "непереходный",
    "masc": "мужской род",
    "femn": "женский род",
    "neut": "средний род",
    "sing": "единственное число",
    "plur": "множественное число",
    "1per": "1 лицо",
    "2per": "2 лицо",
    "3per": "3 лицо",
    "nomn": "именительный падеж",
    "gent": "родительный падеж",
    "datv": "дательный падеж",
    "accs": "винительный падеж",
    "ablt": "творительный падеж",
    "loct": "предложный падеж",
    "voct": "звательный падеж",
    "gen1": "первый родительный",
    "gen2": "второй родительный (частичный)",
    "acc2": "второй винительный",
    "loc1": "первый предложный",
    "loc2": "второй предложный",
    "inan": "неодушевлённое",
    "anim": "одушевлённое",
    "perf": "совершенный вид",
    "impf": "несовершенный вид",
    "NOUN": "существительное",
    "ADJF": "прилагательное (полное)",
    "ADJS": "прилагательное (краткое)",
    "COMP": "сравнительная степень",
    "VERB": "глагол",
    "INFN": "инфинитив",
    "PRTF": "причастие (полное)",
    "PRTS": "причастие (краткое)",
    "GRND": "деепричастие",
    "NUMR": "числительное",
    "ADVB": "наречие",
    "NPRO": "местоимение",
    "PRED": "предикатив",
    "PREP": "предлог",
    "CONJ": "союз",
    "PRCL": "частица",
    "INTJ": "междометие",
    "Qual": "качественное",
}

def analyze_word(word: str) -> dict:
    parsed = morph.parse(word)[0]
    pos = parsed.tag.POS
    grammemes = list(parsed.tag.grammemes)  # множество -> список

    return {
        "pos": pos,
        "pos_ru": GRAMMAR_TRANSLATIONS.get(pos, "неизвестно"),
        "grammar": [GRAMMAR_TRANSLATIONS.get(tag, tag) for tag in grammemes],
        "grammar_ru": [GRAMMAR_TRANSLATIONS.get(tag, tag) for tag in grammemes]
    }