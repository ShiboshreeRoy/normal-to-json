from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="normal_to_json",
    version="1.0.0",
    description="A Python library to convert normal data to JSON.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shiboshree Roy",
    author_email="shiboshreeroy169@gmail.com",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)