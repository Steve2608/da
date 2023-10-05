import pathlib

from setuptools import setup

setup(
    name="da",
    version="0.0.2",
    description="Pytorch domain adaptation package",
    author="Schmid, F. and Masoudian, S.",
    author_email="florian.schmid@jku.at, shahed.masoudian@jku.at",
    url="https://github.com/CPJKU/da",
    license="GPLv2",
    packages=["da"],
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["deep learning", "pytorch", "AI", "domain adaptation"],
    python_requires=">=3.8",
    setup_requires=[],
    install_requires=pathlib.Path("requirements.txt").read_text().split("\n"),
    classifiers=[
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
