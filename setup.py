from setuptools import setup, find_packages

setup(
    name="hivemind",  # Name of the package
    version="0.1.0",  # Package version
    author="Hemang Mohan",
    author_email="hemangshornur@gmail.com",
    description="A modular AI system with agents, tools, and LLM integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemangsrr/hivemind",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "langchain",
    ],
    python_requires=">=3.9",
)
