"""O‘zbekcha kalit so‘zlarni Python sintaksisiga tarjima qilish."""
import ast
import io
import tokenize

class TranslationError(ValueError):
    """Tarjima yoki sintaksisni tekshirishda yuz bergan xato."""

KEYWORDS = {
    "standart": "def", "agar": "if", "aks_holda": "else",
    "aks_holdagar": "elif", "qaytar": "return", "chiqar": "print",
    "uchun": "for", "ichida": "in", "toki": "while",
    "tugat": "break", "davom_et": "continue", "rost": "True",
    "yolgon": "False", "bosh": "None", "va": "and",
    "yoki": "or", "emas": "not", "sinab_kor": "try",
    "xato_bolsa": "except", "nihoyat": "finally", "import_qil": "import",
    "dan": "from", "sifatida": "as", "sinif": "class",
    "oziga": "self", "ochiq": "pass", "oshir": "raise",
    "tasdiqla": "assert", "global_": "global", "mahalliy": "nonlocal",
    "ochish": "with", "asinx": "async", "kut": "await",
}
ERROR_HINTS = {
    "invalid syntax": "Sintaksis xatosi: kod tuzilishini tekshiring.",
    "expected ':'": "Sarlavha oxiriga ikki nuqta (:) qo‘ying.",
    "unexpected indent": "Keraksiz chekinish bor: qator boshidagi bo‘sh joylarni tekshiring.",
    "unindent does not match": "Chekinishlar bir xil emas: probel va tab aralashmaganini tekshiring.",
    "was never closed": "Qavs yoki ifoda yopilmay qolgan.",
    "unterminated string": "Matn satri yopilmagan: qo‘shtirnoqlarni tekshiring.",
}

def translate(source):
    """Kalit so‘zlarni tarjima qiladi; satr va izoh tokenlarini o‘zgartirmaydi."""
    if not isinstance(source, str):
        raise TypeError("source matn (str) bo‘lishi kerak")
    output = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type == tokenize.NAME and tok.string in KEYWORDS:
                tok = tokenize.TokenInfo(tok.type, KEYWORDS[tok.string], tok.start, tok.end, tok.line)
            output.append(tok)
        return tokenize.untokenize(output)
    except (tokenize.TokenError, IndentationError) as exc:
        detail = str(exc)
        if "multi-line string" in detail or "EOF in multi-line statement" in detail:
            detail = "Matn satri yoki qavs yopilmay qolgan."
        raise TranslationError("Kodni tahlil qilib bo‘lmadi: " + detail) from exc

def translate_and_validate(source, filename="<uzpy>"):
    """Tarjima qiladi, Python sintaksisini tekshiradi va tarjima matnini qaytaradi."""
    converted = translate(source)
    try:
        ast.parse(converted, filename=filename)
    except SyntaxError as exc:
        detail = exc.msg or "Noma’lum sintaksis xatosi"
        hint = next((v for k, v in ERROR_HINTS.items() if k in detail.lower()), detail)
        location = "qator {}".format(exc.lineno or "?")
        if exc.offset: location += ", ustun {}".format(exc.offset)
        raise TranslationError("O‘zbekcha kodda sintaksis xatosi ({}): {}".format(location, hint)) from exc
    return converted

def supported_keywords():
    """Kalit so‘zlar lug‘atining mustaqil nusxasini qaytaradi."""
    return dict(KEYWORDS)
