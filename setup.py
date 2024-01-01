import os

from setuptools import find_packages, setup


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith("#", "git+", '"', "-")
    ]


setup(
    name="KrvdDvrkDundie",
    version="0.1.1",
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="KrvdDvrk",
    pyhton_requires=">=3.10",
    packages=find_packages(exclude=["integration"]),
    include_package_data=True,
    entry_points={"console_scripts": ["KrvdDvrkDundie = KrvdDvrkDundie.__main__:main"]},
    install_requires=["click", "rich", "rich-click"],
    extras_require={
        "test": ["pytest", "pytest-forked", "flake8", "pyproject-flake8", "black", "isort"],
        "dev": [
            "ipdb",
            "ipython<=8.0.0",
            "pudb",
            "flake8",
            "pyproject-flake8",
            "black",
            "isort",
            "mkdocs",
            "wheel",
            "twine",
        ],
    },
)
