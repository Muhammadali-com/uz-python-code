# PyPI'ga chiqarishdan oldin

1. `python -m unittest discover -s tests -v`
2. `python -m pip install --upgrade build twine`
3. `python -m build`
4. `python -m twine check dist/*`
5. PyPI hisobida API token yarating va `python -m twine upload dist/*` bilan yuklang.

Tokenni chatga, kodga yoki ommaviy faylga yozmang. PyPI'ga chiqarilgan versiyani ayni versiya raqami bilan qayta yuklab bo‘lmaydi. Ushbu ZIP ichida tayyor `dist/` tarqatmalari yo‘q: ular build jarayonida yaratilishi kerak.
