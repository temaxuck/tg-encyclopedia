from sympy import preview
from io import BytesIO


def convert_latex_to_image(latex_expression: str) -> BytesIO:
    """Convert latex expression to png image

    Args:
        latex_expression (str): LaTeX expression. Note, this function automatically encloses $ around

    Returns:
        BytesIO: Bytes image
    """

    image = BytesIO()

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

    return image
