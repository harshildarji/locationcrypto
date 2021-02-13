import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locationcrypto",
    version="1.0.5",
    author="Harshil Darji",
    author_email="darjiharshil2994@gmail.com",
    description="Location based Cryptography uses location of the device in addition to the pass-phrase as key.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshildarji/locationcrypto",
    packages=setuptools.find_packages(),
    install_requires=['geocoder'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
