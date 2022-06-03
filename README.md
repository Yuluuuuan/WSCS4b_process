# WSCS4b_process
[![build](https://github.com/Yuluuuuan/WSCS4b_process/actions/workflows/build.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_process/actions/workflows/build.yml)
[![unit_test](https://github.com/Yuluuuuan/WSCS4b_process/actions/workflows/unit_test.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_process/actions/workflows/unit_test.yml)

This is a Brane package for data preprocessing. 

Make sure you have brane installed.

Import the package as follows:
```bash
$ brane import Yuluuuuan/WSCS4b_process
```
Set the environment variable. It shows where the data files are.

```bash
$ export FILE='/data'
```

There are two functions in this package:

`create_train_dateset(file: str)` \
`rcreate_test_dateset(file: str)`\
for . We can get corresponding results



You can `test` the package to get an overview of these functions and corresponding parameters:
```bash
$ brane --debug test process
```

You should push the package into your brane instance to be able to import it in your remote session or jupyterlab notebook.
```bash
$ brane push process
```
