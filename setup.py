"""
Setup configuration for Quantum Simulation Scheduling
"""
from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="quantum-simulation-scheduling",
    version="1.0.0",
    author="Quantum Scheduling Team",
    author_email="your.email@example.com",
    description="A quantum circuit scheduling and benchmarking framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1",
    packages=find_packages(exclude=["tests", "docs", ".archive"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
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
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "quantum-bench=benchmarks.comparison.comparison_runner:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
