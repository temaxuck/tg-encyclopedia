from sympy import preview
from io import BytesIO
import re


def convert_latex_to_image(latex_expression: str) -> BytesIO:
    """Convert latex expression to png image

    Args:
        latex_expression (str): LaTeX expression. Note, this function automatically encloses $ around

    Returns:
        BytesIO: bytes that represent image
    """

    image = BytesIO()

    latex_expression = re.sub(
        r"(\S)\s*<\s*(\S)", r"\1 \\textless{} \2", latex_expression
    )

    latex_expression = re.sub(
        r"(\S)\s*>\s*(\S)", r"\1 \\textgreater{} \2", latex_expression
    )

    preview(
        f"${latex_expression}$",
        output="png",
        viewer="BytesIO",
        outputbuffer=image,
        euler=False,
        dvioptions=[
            "-T",
            "tight",
            "-z",
            "0",
            "--truecolor",
            "-D 600",
        ],
    )

    image.seek(0)

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
