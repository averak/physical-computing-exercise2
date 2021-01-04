# 物理手書き文字認識

実世界情報演習 2 の自由課題

## Description

This project's objective is to recognize physically written characters.

You are only allowed to enter numbers. After writing the numerical value, the recognition result is displayed on the 7seg LED.

## Architecture

![](./image/architecture.png)

## Requiremenst

- Python ~> 3.8
- pipenv

## Installation

If you don't have pipenv installed, see [documents](https://github.com/pypa/pipenv).

```sh
$ git clone <this repo>
$ cd <this repo>

$ cd src
$ pipenv install
```

## Usage

See `scripts` section of [Pipfile](./src/Pipfile)

- `pipenv run test`
- `pipenv run format`
- `pipenv run lint`

### Show help

```sh
$ ./app.py -h
```

### Record teacher data

```sh
$ ./app.py --record
```

### Training

```sh
$ ./app.py --train # --dim <DIM>
```

### Infer

```sh
$ ./app.py --infer --port <serial port> # --dim <DIM>
```
