import os
from pkg_resources import parse_requirements

from importlib.machinery import SourceFileLoader
from setuptools import find_packages, setup

module_name = "tg_encyclopedia"

module = SourceFileLoader(
    module_name, os.path.join(module_name, "__init__.py")
).load_module()


def load_requirements(filepath: str) -> list:
    requirements = []

    with open(filepath, "r") as fp:
        for req in parse_requirements(fp.read()):
            extras = "[{}]".format(",".join(req.extras) if req.extras else "")
            requirements.append("{}{}{}".format(req.name, extras, req.specifier))

    return requirements


setup(
    name=module_name,
    version=module.__version__,
    author=module.__author__,
    author_email=module.__email__,
    license=module.__license__,
    description=module.__doc__,
    long_description=open("README.rst", "r").read(),
    url="https://github.com/temaxuck/tg-encyclopedia",
    platforms="all",
    python_requires=">=3.10",
    packages=find_packages(exclude=["tests"]),
    install_requires=load_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "oenp-bot = {0}.bots.oenp_bot.__main__:run_bot".format(module_name),
            "oenp-channel = {0}.bots.oenp_channel_bot.__main__:load_pyarmids_to_channel".format(
                module_name
            ),
        ]
    },
    include_package_data=True,
)
