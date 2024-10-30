from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="",
    vertion="0.0.1",
    author="Rodrigo M.",
    author_email="rodrigofmacarini@gmail.com",
    description="Calculator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    python_requires='=>3.8',
)