import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="psychedelic"
    version="0.0.1",
    author="wilnelys roman",
    author_email="wilnelys11@hotmail.com",
    url="https://github.com/wroman191/psychedelic",
    description="what does yourproject do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
