# shm developer wiki

[[_TOC_]]

`shm` is a [defenselayers](https://defenselayers) __secure harbour__ manifest tool listing all available
container images in both production and testing registries.

## Installing development tools
`devel-requirements.txt` file contains development tools like `pytest` required for development related tasks.

`requirements.txt` contains only dependencies needed to run `shm` however you do not need to install those
separately as they are already installed by `setup.py`.

```bash
$ cd ./shm
$ pip3 install -r devel-requirements.txt
```

## Installing shm in development mode
Since `shm` is [click](https://click.palletsprojects.com/en/7.x/) based application it is tightly integrated with
`setuptools`. To install it in development mode use `pip3`:
```bash
$ cd ./shm
$ pip3 install -e .
```  

> Do not forget about installing development tools.

## Building wheel
```bash
$ cd ./shm
$ pip3 install -r devel-requirements.txt
$ python setup.py sdist bdist_wheel
```

## Running tests with coverage
```bash
$ cd ./shm
$ pip3 install -r devel-requirements.txt
$ pytest --cov=shmanifest --pep8 ./test/
```