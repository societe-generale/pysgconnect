from os import path
from setuptools import find_packages, setup

requirements_path = path.join(path.dirname(__file__), "requirements.txt")
readme_path = path.join(path.dirname(__file__), "README.md")

with open(readme_path, "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(requirements_path, "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="pysgconnect",
    version="2.3",
    url="https://github.com/societe-generale/pysgconnect",
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Utilities to interact with SGConnect",
    python_requires=">=3.10",
    include_package_data=True,
    package_data={"": [readme_path, requirements_path]},
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
        "Natural Language :: French",
        "Natural Language :: English",
        "Environment :: MacOS X",
        "Environment :: Web Environment",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Environment :: OpenStack",
        "Environment :: Console",
        "Environment :: Plugins",
        "Environment :: No Input/Output (Daemon)",
        "Environment :: Other Environment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: Other/Proprietary License"
    ],
)
