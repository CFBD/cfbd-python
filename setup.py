# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.11
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "cfbd"
VERSION = "5.6.11"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="College Football Data API",
    author_email="admin@collegefootballdata.com",
    url="https://github.com/CFBD/cfbd-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "College Football Data API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description="""\
    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.
    """,  # noqa: E501
    package_data={"cfbd": ["py.typed"]},
)
