import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Escher",
    version="0.0.1",
    author="Sanjeev Mk",
    author_email="sanjeevmk4890@gmail.com",
    description="A 3D editing and rendering framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanjeevmk/Escher",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['scipy',
                      'numpy',
                      'trimesh'
                      ],
    python_requires=">=3.6",
)
