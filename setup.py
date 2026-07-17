"""
Veritas-Core Agent Runtime Framework

Install: pip install -e .
Usage:   veritas run --task "analyze" --agent "evaluator"
"""
from setuptools import setup, find_packages

setup(
    name="veritas-core",
    version="7.0.0",
    description="Veritas Agent Runtime Framework — pluggable, observable, recoverable",
    packages=find_packages(where=".", include=["veritas", "veritas.*"]),
    package_dir={"": "."},
    entry_points={
        "console_scripts": [
            "veritas = veritas.cli.main:main",
        ],
    },
    python_requires=">=3.10",
    install_requires=[
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
        ],
        "all": [
            "fastapi",
            "uvicorn",
            "streamlit",
        ],
    },
)
