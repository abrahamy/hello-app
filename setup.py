# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["hello_app", "hello_app.api", "hello_app.services"]

package_data = {"": ["*"]}

setup_kwargs = {
    "name": "hello-app",
    "version": "0.1.0",
    "description": "Hello App",
    "long_description": None,
    "author": "Abraham Yusuf",
    "author_email": "aaondowasey@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/abrahamy/hello-app",
    "packages": packages,
    "package_data": package_data,
    "python_requires": ">=3.8,<4.0",
}


setup(**setup_kwargs)
