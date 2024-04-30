from pip import download, req
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

links = []
requires = []

try:
    requirements = req.parse_requirements("requirements.txt")
except:
    requirements = req.parse_requirements(
        "requirements.txt", session=download.PipSession()
    )

for item in requirements:
    if getattr(item, "url", None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, "link", None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

setup(
    name="pysgconnect",
    version="1.0",
    url="https://github.com/societe-generale/pysgconnect",
    package_dir={'':"pysgconnect"},
    packages=find_packages(),
    install_requires=requires,
    dependency_links=links,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Utilities to interact with SGConnect",
    python_requires=">=3.10",
    build-backend="setuptools.build_meta",
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
)
