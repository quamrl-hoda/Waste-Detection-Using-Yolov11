import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()

__version = "0.0.1"

REPO_NAME = "Waste-Detection-Using-Yolov11"
AUTHOR_USER_NAME = "quamrl-hoda"
SRC_REPO = "wasteDetection"
AUTHOR_EMAIL = "qhoda434@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version,  
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A project to detect waste using YOLOv11",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)