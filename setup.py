from setuptools import setup, find_packages

setup(
    name="gameutils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    author="Chris Williamson",
    description="Reusable game development utilities",
)