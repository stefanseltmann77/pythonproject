# run:   >>>python setup.py bdist_wheel
# for building a wheel
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="my_project",
    version="0.1.0",
    author="Your Name",
    author_email="Your Mail",
    description="my_project ... described",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url='gitlink_if_necessary',
    packages=['my_project_module'],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
