import io
from typing import Any

import qrcode


def generate_simple_qr_by_url(url: str) -> Any:
    img = qrcode.make(url)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    # img.save(f"generated_data/{url}.png")
    return img_byte_arr.getvalue()

