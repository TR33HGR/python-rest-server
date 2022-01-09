import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-rest-server-tr33hgr", # Replace with your own username
    version="0.0.1",
    author="TR33HGR",
    author_email="",
    description="A Rest server for debugging RestApi calls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TR33HGR/python-rest-server",
    project_urls={
        "Bug Tracker": "https://github.com/TR33HGR/python-rest-server/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
          'flask',
          'python-dotenv',
    ],
    python_requires=">=3.6",
)