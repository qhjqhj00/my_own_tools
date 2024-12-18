from setuptools import setup, find_packages

setup(
    name="my_own_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "openai",
        "scipy",
        "pandas",
    ],
    author="",
    author_email="",
    description="A collection of personal tools and utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
