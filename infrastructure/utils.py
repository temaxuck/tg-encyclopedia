from sympy import preview
from io import BytesIO
import cv2
import re
import numpy as np


def convert_latex_to_image(
    latex_expression: str, font_size: float = 40, padding: int = 10
) -> BytesIO:
    """Convert latex expression to png image

    Args:
        latex_expression (str): LaTeX expression. Note, this function automatically encloses $ around
        font_size (float): size of font in pixels. Note, that the less font_size, the less image resolution
        padding (int): size of padding in pixels.

    Returns:
        BytesIO: bytes representation of image
    """

    def produce_tex_image(latex_expression):
        tex_image = BytesIO()

        preview(
            f"${latex_expression}$",
            output="png",
            viewer="BytesIO",
            outputbuffer=tex_image,
            euler=False,
            dvioptions=[
                "-T tight",
                "-z",
                "0",
                "--truecolor",
                f"-D {font_size * 72.27 / 10}",
            ],
        )

        tex_image.seek(0)

        return tex_image

    def produce_image_with_padding(image_bytes):
        image_bytes = image_bytes.getvalue()

        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        top, bottom, left, right = [padding] * 4
        color = [255, 255, 255]

        image_with_padding = cv2.copyMakeBorder(
            image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color
        )
        _, buffer = cv2.imencode(".png", image_with_padding)

        return BytesIO(buffer.tobytes())

    latex_expression = re.sub(
        r"(\S)\s*<\s*(\S)", r"\1 \\textless{} \2", latex_expression
    )

    latex_expression = re.sub(
        r"(\S)\s*>\s*(\S)", r"\1 \\textgreater{} \2", latex_expression
    )

    tex_image = produce_tex_image(latex_expression)
    image = produce_image_with_padding(tex_image)

    return image


def get_pyramid_latex_representation(
    sequence_number: int, gf_latex: str, ef_latex: str
) -> str:
    """
    Get pyramid's latex representation by generating function's and explicit formula's latex representations

    Args:
        sequence_number (int): pyramid's sequence number
        gf_latex (str): pyramid's generating function's latex representation
        ef_latex (str): pyramid's explicit formula's latex representation

    Returns:
        str: pyramid's latex representation that would be passed to convert_latex_to_image to image
    """

    return (
        r"\text{" + f"Pyramid {sequence_number}" + r"} \\ \\"
        r"\text{Generating function} \\" + f"{gf_latex}" + r" \\ \\"
        r"\text{Explicit formula} \\" + f"{ef_latex}"
    )


def get_formatted_gf_latex(gf_latex: str):
    """
    Get formatted latex representation of generating function of pyramid

    Args:
        gf_latex (str): generating function's latex representation
    """

    return r"\text{Generating function} \\" + f"{gf_latex}" + r" \\ \\"


def get_formatted_ef_latex(ef_latex: str):
    """
    Get formatted latex representation of explicit formula of pyramid

    Args:
        ef_latex (str): explicit formula's latex representation
    """

    return r"\text{Explicit formula} \\" + f"{ef_latex}"
