"""Setup script dla my_awesome_lib."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="my-awesome-lib",
    version="1.0.0",
    author="Twoje Imię",
    author_email="twoj.email@example.com",
    description="Biblioteka narzędziowa do przetwarzania danych, obliczeń matematycznych i tekstu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/twoj-username/my-awesome-lib",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=4.0",
            "black>=22.0",
            "mypy>=0.900",
        ],
    },
)
