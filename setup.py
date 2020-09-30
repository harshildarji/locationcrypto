import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="location-cryptography", #Feel free to change this! 
    version="1.0.0",
    author="Author", #Fill this out
    author_email="author@example.com", #fill this out
    description="A small example package", #fill this out
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshildarji/location_based_cryptography",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
