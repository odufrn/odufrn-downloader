import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="odufrn_downloader",
    version="0.1.5",
    author="Open Data UFRN",
    author_email="alvarofepipa@gmail.com",
    description="Open Data UFRN Downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/odufrn/odufrn-downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
