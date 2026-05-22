from setuptools import setup, find_packages

setup(
    name="kh2md",
    version="0.1.0",
    description="Convert Kindle highlights to Markdown",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Femirins",
    author_email="femirins@localhost",
    url="https://github.com/femirins/kh2md",
    py_modules=["kh2md"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "kh2md=kh2md:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)