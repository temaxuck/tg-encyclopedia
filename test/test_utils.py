import infrastructure.utils as utils


def test_get_pyramid_latex_representation():
    expected_out = r"\text{Pyramid #1} \\ \\\text{Generating function} \\U_{1}(x, y) = x + y \\ \\\text{Explicit formula} \\\delta{(a, b)} = \begin{cases}1&\text{if a = b},\\ 0  \end{cases}  \\ T_{1}(n, m, k) = \delta{\left(k,m + n \right)} {\binom{m + n}{m}}"
    input_values = (
        1,
        "U_{1}(x, y) = x + y",
        "\\delta{(a, b)} = \\begin{cases}1&\\text{if a = b},\\\\ 0  \\end{cases}  \\\\ T_{1}(n, m, k) = \\delta{\\left(k,m + n \\right)} {\\binom{m + n}{m}}",
    )
    assert expected_out == utils.get_pyramid_latex_representation(input_values)


def test_convert_latex_to_image():
    from PIL import Image
    import io

    latex_expression = r"U_{323}(x, y) = \frac{2 y + \sqrt{1 - 4 y} + \sqrt{2} \sqrt{4 x y^{3} + 2 y^{2} - 4 y + \sqrt{1 - 4 y} \left(- 4 x y^{3} + 2 y - 1\right) + 1} - 1}{2 y \sqrt{1 - 4 y} - 2 y} \\ T_{323}(n, m, k) = \begin{cases}0&\text{if n < k} ,\ \\\frac{\left(-1\right)^{n} k {\binom{- k + 2 n - 1}{n - 1}}}{n}&\text{if m=0} ,\ \\\frac{\left(-1\right)^{n} \left(-1\right)^{m - 1} k \left(k - 3 n\right) {\binom{- k + 2 n - 1}{n - 1}} {\binom{- k - m + 3 n - 1}{m - 1}}}{m n} \end{cases} "

    image_bytes = utils.convert_latex_to_image(latex_expression)
    image = Image.open(io.BytesIO(image_bytes))
    image.save("test-output.png", "PNG")
