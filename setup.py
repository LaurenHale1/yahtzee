import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yahtzee",
    version="0.0.1",
    author="Hostedposted",
    author_email="hostedpostedsite@gmail.com",
    description="Yahtzee game in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hostedposted/yahtzee",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)