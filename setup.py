from setuptools import setup

with open("README.md", "rt") as fin:
    long_description = fin.read()

setup(
    name="shm",
    version="0.1",
    author="Aleksander P. Czarnowski",
    description="Defenselayers secure harbour manifest tool (container registry utility).",
    long_description=long_description,
    url="https://github.com/defenselayers/shm",
    py_modules=["shmanifest"],
    include_package_data=True,
    install_requires=["click",
                      "colorama",
                      "requests"],
    entry_points="""
        [console_scripts]
        shm=shmanifest:cli
    """,
    python_requires=">=3.5",
)
