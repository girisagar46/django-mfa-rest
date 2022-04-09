import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
PROJECT_NAME = "django-mfa-rest"

data_files = []
for dir_path, dir_names, filenames in os.walk(PROJECT_NAME):
    for i, dirname in enumerate(dir_names):
        if dirname.startswith("."):
            del dir_names[i]
    if "__init__.py" in filenames:
        continue
    elif filenames:
        data_files.extend(
            os.path.join(dir_path[len(PROJECT_NAME) + 1 :], f) for f in filenames
        )

install_requires = [
    "Django",
    "django-argonauts",
    "python-u2flib-server",
    "qrcode",
]

setup(
    name="django-mfa-rest",
    version="1.0.0",
    packages=[
        "django_mfa_rest",
        "django_mfa_rest.templatetags",
        "django_mfa_rest.migrations",
    ],
    include_package_data=True,
    description="A Django package to satisfy your MFA requirements based on REST API. This package is a fork of "
    "django-mfa: https://github.com/micropyramid.",
    long_description=README,
    url="https://github.com/girisagar46/django-mfa-rest",
    author="girisagar46",
    author_email="girisagar46@gmail.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django, Django Rest Framework",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "Django>=3.1.14,<=3.2.12",
        "djangorestframework>=3.12.1,<=3.13.1",
    ],
)
