from setuptools import setup, find_packages

setup(
    name="synametrix",
    version="1.0.0",
    author="Sourish Senapati",
    author_email="sourish.senapati@example.com",
    description="Physics-informed computational models validating thermodynamic constraints and chemical OPEX of AD and Microalgae Biorefineries.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/Synametrix",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "matplotlib>=3.7.0"
    ],
    entry_points={
        "console_scripts": [
            "synametrix=synametrix.cli:main",
        ],
    },
)
