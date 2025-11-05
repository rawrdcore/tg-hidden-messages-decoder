#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict

# Список пар (точка, вариант)
PAIRS = [
    ("⠤", "А"), ("⠱", "а"), ("⠱", "4"),
    ("⠨", "Б"), ("⠲", "б"), ("⠲", "5"),
    ("⠰", "В"), ("⠴", "в"), ("⠴", "6"),
    ("⡁", "Г"), ("⡁", " "),
    ("⠸", "г"), ("⠸", "7"),
    ("⡂", "Д"), ("⡃", "д"), ("⡃", "8"),
    ("⡄", "Е"), ("⡅", "е"), ("⡅", "9"),
    ("⠠", "Ё"), ("⢨", "ё"),
    ("⡈", "Ж"), ("⡆", "ж"), ("⡆", ":"),
    ("⡐", "З"), ("⡉", "з"), ("⡉", ";"),
    ("⡠", "И"), ("⡊", "и"), ("⡊", "<"),
    ("⢁", "Й"), ("⡌", "й"), ("⡌", "="),
    ("⢂", "К"), ("⡑", "к"), ("⡑", ">"),
    ("⢄", "Л"), ("⡒", "л"), ("⡒", "?"),
    ("⢑", "М"), ("⡍", "м"),
    ("⢈", "Н"), ("⡔", "н"), ("⡔", "@"),
    ("⢐", "О"), ("⡘", "о"),
    ("⢔", "П"), ("⡓", "п"),
    ("⣀", "Р"), ("⣀", "#"), ("⡢", "р"),
    ("⠇", "С"), ("⠇", "$"), ("⡨", "с"),
    ("⠋", "Т"), ("⠋", "%"), ("⡰", "т"),
    ("⠍", "У"), ("⠍", "&"), ("⢃", "у"),
    ("⠓", "Ф"), ("⠓", "("), ("⢅", "ф"),
    ("⠕", "Х"), ("⠕", ")"), ("⢆", "х"),
    ("⠖", "Ц"), ("⠖", "*"), ("⢉", "ц"),
    ("⠙", "Ч"), ("⠙", "+"), ("⢊", "ч"),
    ("⠚", "Ш"), ("⠚", ","), ("⢌", "ш"),
    ("⠜", "Щ"), ("⠜", "-"), ("⢑", "щ"),
    ("⠣", "Ъ"), ("⠣", "."), ("⢒", "ъ"),
    ("⠥", "Ы"), ("⠥", "/"), ("⢔", "ы"),
    ("⠦", "Ь"), ("⠦", "0"), ("⢘", "ь"),
    ("⠩", "Э"), ("⠩", "1"), ("⢡", "э"),
    ("⠪", "Ю"), ("⠪", "2"), ("⢢", "ю"),
    ("⠬", "Я"), ("⠬", "3"), ("⢤", "я"),
    ("⡁", "пробел"),
    ("⡂", "!"), ("⢠", '"'), ("⠸", "№"), ("⡉", ";"), ("⠋", "%"),
    ("⡆", ":"), ("⡒", "?"), ("⠖", "*"), ("⠓", "("), ("⠕", ")"),
    ("⠝", "_"), ("⠙", "+"), ("⠜", "-"), ("⡌", "="), ("⡔", "@"),
    ("⣀", "#"), ("⠇", "$"), ("⠛", "^"), ("⠍", "&"), ("⠞", "`"),
    ("⡸", "~"), ("⠏", "\\"), ("⡲", "|"), ("⠥", "/"), ("⡑", ">"),
    ("⡊", "<"), ("⠚", ","), ("⠣", "."),
]

# Словари
BRAILLE_MAP = OrderedDict()
for dot, val in PAIRS:
    if dot not in BRAILLE_MAP:
        BRAILLE_MAP[dot] = []
    if val not in BRAILLE_MAP[dot]:
        BRAILLE_MAP[dot].append(val)

ENCODE_MAP = OrderedDict()
for dot, val in PAIRS:
    if val not in ENCODE_MAP:
        ENCODE_MAP[val] = dot

# --- Функции ---

def decode(text):
    """Преобразует точки в буквы"""
    for ch in text:
        if ch in BRAILLE_MAP:
            variants = BRAILLE_MAP[ch]
            pretty = [v if v != " " else "пробел" for v in variants]
            print(f"{ch} -> " + ", ".join(pretty))
        else:
            print(f"{ch} -> ? (неизвестно)")

def encode(text):
    """Преобразует текст в точки"""
    result = []
    for ch in text:
        if ch == " ":
            ch = "пробел"
        if ch in ENCODE_MAP:
            result.append(ENCODE_MAP[ch])
        elif ch.lower() in ENCODE_MAP:
            result.append(ENCODE_MAP[ch.lower()])
        else:
            result.append("?")
    print("".join(result))

# --- Основной блок ---

def main():
    if len(sys.argv) < 3:
        print("Использование:")
        print("  python braille_decoder.py --decode \"⠬⡁⡒⢢⠲⡒\"")
        print("  python braille_decoder.py --encode \"Привет\"")
        sys.exit(1)

    mode = sys.argv[1]
    text = sys.argv[2]

    if mode == "--decode":
        decode(text)
    elif mode == "--encode":
        encode(text)
    else:
        print("Ошибка: укажи --encode или --decode")

if __name__ == "__main__":
    main()
