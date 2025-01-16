from typing import Tuple
import json
import re
from mySecrets import hexToStr
import traceback
import fitz


__all__ = ['binary_to_str', 'pdf_to_png_bytes']

def binary_to_str(data: bytes) -> str:
    try:
        return data.decode('utf-8')
    except:
        return str(data)[2:-1]

def pdf_to_png_bytes(pdf_path, dpi=300):
    document = fitz.open(pdf_path)
    if document.page_count > 0:
        page = document.load_page(0)
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        result = pix.tobytes("png")
        # os.remove(pdf_path)
        return result