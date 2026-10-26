"""UzCodepackage: Python uchun o‘zbekcha kalit so‘zlar tarjimoni."""
from .translator import KEYWORDS, TranslationError, translate, translate_and_validate, supported_keywords
__version__ = "1.0.0"
__all__ = ["__version__", "KEYWORDS", "TranslationError", "translate", "translate_and_validate", "supported_keywords"]
