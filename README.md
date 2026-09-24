# Library Data Pipeline

A small data pipeline that cleans a library's loan records, tests the cleaning,
and ships it in a container. Built for AEDXDDE5M5 Product Development, exercises
2 to 6.

The library system exports two CSV files. They are messy in the ways real
exports usually are: blank padding rows, dates wrapped in stray quote marks,
a borrowing period recorded as the words "2 weeks", loans returned before they
were taken out, and customers referenced that do not exist. This project turns
that into something you can present.

## What is in here

| Path | What it is |
| --- | --- |
| `src/main.py` | The entry point. Reads, cleans, writes. |
| `src/cleaning_module.py` | The cleaning functions, one job each. |
| `src/class_file.py` | A small Calculator class, used by the testing exercise. |
| `testing/` | The pytest and unittest suites. |
| `data/` | Input CSVs. Read only, never edited in place. |
| `data/processed/` | Output. Regenerated on every run. |
| `docker/Dockerfile` | Builds the image. |
| `docker/commands.txt` | Docker command notes. |
| `.github/workflows/` | GitHub Actions: tests, then the image build. |
| `pipeline/` | Azure Pipelines equivalents. |
| `requirements.txt` | Python dependencies. |

## Getting started

Python 3.12 or later, then from the repo root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running it

```bash
python src/main.py
```

Reads `data/library.csv` and `data/library_customers.csv`, writes
`library_clean.csv` and `library_customers_clean.csv` into `data/processed/`.
Paths are resolved relative to the project root, so it runs from anywhere.

## Running the tests

```bash
python -m pytest testing/ -v
```

Both styles are here on purpose: `test_calc_py_test.py` uses pytest with plain
asserts and fixtures, `test_calc_unit_test.py` uses `unittest.TestCase` with
`setUp` and the assert methods. pytest collects both.

The unittest suite also runs on its own:

```bash
python -m unittest discover -s testing -v
```

## Docker

The build context is the repo root, and the Dockerfile lives in `docker/`, so
the build needs `--file`:

```bash
docker build --file docker/Dockerfile --tag library-pipeline:1.0 .
```

```bash
docker run --rm --volume "${PWD}/data/processed:/app/data/processed" library-pipeline:1.0
```

The volume mount matters. A container is disposable: without it the pipeline
writes its output inside the container, the container exits, and the files go
with it.

`.dockerignore` keeps `.venv`, `.git` and the generated output out of the image.
Docker does not read `.gitignore`, so the two files have to be maintained
separately.

## Continuous integration

Three workflows, all on push and pull request to `main`, and all runnable by
hand from the Actions tab:

| Workflow | What it does |
| --- | --- |
| `testing_ci.yml` | Installs dependencies, runs the tests, then builds the Docker image and uploads it as an artefact. |
| `example_workflow.yml` | A minimal workflow, kept as a reference. |
| `secret_demo.yml` | Shows how a secret is passed to a step without it appearing in the log. |

Secrets are never committed. They are set in the repository settings and read
at run time. A secret that reaches git is leaked even after the line is
deleted, because the history keeps it.

## The data

`library.csv` is 114 rows, of which 93 are entirely blank. There are 21 real
loans. Any percentage calculated from the raw row count is wrong by roughly
five times, which is the first thing the cleaning fixes.

Known faults in the source data, all deliberate:

- 93 blank rows, and one real loan missing both title and customer
- checkout dates wrapped in doubled quote marks, so they read as text
- one date of `32/05/2023`, which is not a date
- one checkout in 2063
- six loans returned before they were checked out
- the borrowing period held as the words `2 weeks`
- the same loan entered twice under two different `Id` values
- customers 4 and 10 referenced by loans but absent from the customer file
