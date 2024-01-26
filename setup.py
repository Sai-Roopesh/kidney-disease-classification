import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


__version__ = '0.0.0'

REPO_NAME = 'kidney_disease_classification'
AUTHOR_NAME = 'Sai-Roopesh'
SRC_REPO = 'Kidney_disease_classification'
AUTHOR_EMAIL = 'sairoopesh21@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Kidney Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Sai-Roopesh/kidney-disease-classification",
    project_urls={
        "Bug Tracker": f"https://github.com/Sai-Roopesh/kidney-disease-classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
