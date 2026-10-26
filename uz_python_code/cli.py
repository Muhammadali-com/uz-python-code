"""uzpy buyruq qatori interfeysi."""
import argparse
import os
from pathlib import Path
import sys
from . import __version__
from .translator import TranslationError, translate_and_validate

def _read(path):
    try: return Path(path).read_text(encoding="utf-8")
    except OSError as exc: raise RuntimeError("Faylni o‘qib bo‘lmadi: {} ({})".format(path, exc)) from exc

def _write(path, content):
    try: Path(path).write_text(content, encoding="utf-8")
    except OSError as exc: raise RuntimeError("Natijani yozib bo‘lmadi: {} ({})".format(path, exc)) from exc

def build_parser():
    parser = argparse.ArgumentParser(prog="uzpy", description="O‘zbekcha Python kodini tarjima qilish, tekshirish va ishga tushirish.")
    parser.add_argument("--version", action="version", version="uz-python-code {}".format(__version__))
    sub = parser.add_subparsers(dest="command")
    tr = sub.add_parser("translate", help="Oddiy Python kodiga tarjima qilish"); tr.add_argument("file"); tr.add_argument("-o", "--output")
    check = sub.add_parser("check", help="Sintaksisni tekshirish"); check.add_argument("file")
    run = sub.add_parser("run", help="Tarjima qilib ishga tushirish"); run.add_argument("file"); run.add_argument("script_args", nargs=argparse.REMAINDER)
    return parser

def main(argv=None):
    parser = build_parser(); args = parser.parse_args(argv)
    if not args.command: parser.print_help(); return 0
    try:
        converted = translate_and_validate(_read(args.file), filename=args.file)
        if args.command == "translate":
            if args.output: _write(args.output, converted); print("Tarjima saqlandi: {}".format(args.output))
            else:
                sys.stdout.write(converted)
                if converted and not converted.endswith("\n"): sys.stdout.write("\n")
            return 0
        if args.command == "check": print("To‘g‘ri: {} — sintaksis tekshirildi.".format(args.file)); return 0
        source_path = Path(args.file).resolve()
        old_cwd, old_argv, old_path = os.getcwd(), sys.argv[:], sys.path[:]
        sys.argv = [str(source_path)] + list(args.script_args or [])
        sys.path.insert(0, str(source_path.parent)); os.chdir(str(source_path.parent))
        try:
            namespace = {"__name__": "__main__", "__file__": str(source_path), "__package__": None, "__cached__": None}
            exec(compile(converted, str(source_path), "exec"), namespace)
        finally:
            os.chdir(old_cwd); sys.argv = old_argv; sys.path[:] = old_path
        return 0
    except (RuntimeError, TranslationError, SyntaxError) as exc:
        print("Xato: {}".format(exc), file=sys.stderr); return 1

if __name__ == "__main__": raise SystemExit(main())
