from setuptools import find_packages, setup

setup(
    name="final",
    packages=find_packages(exclude=["final_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
