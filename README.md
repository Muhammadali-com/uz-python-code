# UzCodepackage — uz-python-code 1.0.0

**O‘zbekcha Python** — Python kodini o‘zbekcha kalit so‘zlar bilan yozish va uni Python sintaksisiga tarjima qilib ishga tushirish vositasi.

## O‘rnatish

```bash
pip install uz-python-code
```

Yangilash: `pip install --upgrade uz-python-code`

## Birinchi dastur

`salom.py` fayliga yozing:

```python
ism = "Ali"
agar ism:
    chiqar(f"Salom, {ism}!")
```

Ishga tushirish: `uzpy run salom.py`

## Buyruqlar

- `uzpy run fayl.py` — tarjima qiladi va ishga tushiradi.
- `uzpy check fayl.py` — sintaksisni tekshiradi.
- `uzpy translate fayl.py` — tarjimani terminalga chiqaradi.
- `uzpy translate fayl.py -o natija.py` — tarjimani faylga saqlaydi.
- `uzpy --version` — versiyani ko‘rsatadi.

## Kalit so‘zlar

| O‘zbekcha | Python |
|---|---|
| `standart` | `def` |
| `agar` | `if` |
| `aks_holda` | `else` |
| `aks_holdagar` | `elif` |
| `qaytar` | `return` |
| `chiqar` | `print` |
| `uchun` | `for` |
| `ichida` | `in` |
| `toki` | `while` |
| `tugat` | `break` |
| `davom_et` | `continue` |
| `rost` / `yolgon` / `bosh` | `True` / `False` / `None` |
| `va` / `yoki` / `emas` | `and` / `or` / `not` |
| `sinab_kor` / `xato_bolsa` / `nihoyat` | `try` / `except` / `finally` |
| `import_qil` / `dan` / `sifatida` | `import` / `from` / `as` |
| `sinif` / `oziga` / `ochiq` | `class` / `self` / `pass` |
| `oshir` / `tasdiqla` / `global_` / `mahalliy` | `raise` / `assert` / `global` / `nonlocal` |
| `ochish` / `asinx` / `kut` | `with` / `async` / `await` |

Kalit so‘zlar faqat kod tokeni sifatida uchraganda tarjima qilinadi; matn satrlari va izohlar o‘zgartirilmaydi.

## Python API

```python
from uz_python_code import translate, translate_and_validate
kod = translate_and_validate('agar rost:\n    chiqar("Salom")')
print(kod)
```

## Chegaralar

Bu alohida interpreter emas: tarjima qilingan kodni Python bajaradi. Barcha Python konstruksiyalariga o‘zbekcha muqobil yoki har bir tashqi kutubxona bilan to‘liq moslik kafolatlanmaydi. Faqat yuqoridagi kalit so‘zlar tarjima qilinadi; qolgan sintaksis odatdagi Python sintaksisi bo‘lib qoladi. `uzpy run` kodni bajaradi — faqat ishonchli fayllarni ishga tushiring.

## Loyiha tuzilishi

- `uz_python_code/` — paket manba kodi
- `tests/` — avtomatik testlar
- `examples/` — namuna kodlar
- `site/` — InfinityFree hostingga alohida yuklash uchun statik sayt
