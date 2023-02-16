# type: ignore

import nox


@nox.session(python=["3.11"])
def format_code(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("isort", ".", external=True)
    session.run("black", ".", external=True)


@nox.session(python=["3.11"])
def check_code_formatting(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("isort", ".", "--check", "--verbose", external=True)
    session.run("black", ".", "--check", external=True)


@nox.session(python=["3.11"])
def check_static_typing(session):
    session.run("poetry", "install", "--only", "static_type_checking", external=True)
    session.run("poetry", "install", "--only", "testing", external=True)
    session.run("mypy", ".", external=True)


@nox.session(python=["3.11"])
def lint(session):
    session.run("poetry", "install", "--only", "linting", external=True)
    session.run("ruff", "check", ".", "--verbose", external=True)


@nox.session(python=["3.11"])
def run_all_tests(session):
    session.run("poetry", "install", "--only", "testing", external=True)
    session.run("pytest", external=True)


@nox.session(python="3.11")
def upload_coverage_report(session):
    session.run("poetry", "install", "--only", "code_coverage_reporting", external=True)
    session.run("pytest", external=True)
    session.run("codecov", external=True)
