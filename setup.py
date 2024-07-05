import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "omkar"
SRC_REPO = "myml_project"
AUTHOR_EMAIL = "omkarrathod505010@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,  # Corrected syntax
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,  # Corrected spelling
    long_description_content_type="text/markdown",  # Corrected spelling and syntax
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")  # Corrected syntax
)
