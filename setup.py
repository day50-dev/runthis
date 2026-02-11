from setuptools import setup, find_packages

setup(
    name="runthis",
    version="1.0.0",
    description="Run code from GitHub in one command",
    author="RunThis",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "openai>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "runthis=runthis.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)