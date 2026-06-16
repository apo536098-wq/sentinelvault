from setuptools import setup, find_packages

setup(
    name="sentinelvault",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "flask",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "sentinelvault=sentinelvault.cli:main",
        ],
    },
)
