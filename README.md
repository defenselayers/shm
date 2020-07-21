# shm
`shm` is a [defenselayers](https://defenselayers) __secure harbour__ manifest tool listing all available
container images in both production and testing registries.

> `shm` requires credentials from [defenselayers](https://defenselayers) to access __secure harbour__ registries.
> You can use `shm` to access 3rd party container registries providing proper credentials assuming registry is
> using http basic auth.

## Requirements
 * Python 3
 * pip3
 * requests
 * click

Except `Python 3` and `pip3` all other requirements are downloaded and installed during installation.

## Installation
```bash
$ cd ./shm
$ pip install .
``` 

## Running
To list secure images in [defenselayers](https://defenselayers) __secure harbour__ registries just run `shmanifest`:
```bash
$ shm
```

`shm` will ask about user credentials (user name and password). You can optionally provide user name using `-u`
option and password using `-p` option. Alternatively you can provide credentials using environment variables:
 * `SHMANIFEST_USER`
 * `SHMANIFEST_PASSWD`

For example on Windows:
```bash
set SHMANIFEST_USER=user
```

On Linux:
```bash
$ export SHMANIFEST_USER=user
```

To get more verbose output use `-v` option.

## Getting help
To list all available option run `shm` with `--help` switch.

## For developers
If you are a developer you can find further development details in `wiki` directory.
