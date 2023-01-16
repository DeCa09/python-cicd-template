import nox


@nox.session(python=["3.11"])
def format(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("black", ".")


@nox.session(python=["3.11"])
def check_formatting(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("black", ".", "--check")


@nox.session(python=["3.11"])
def check_static_typing(session):
    session.run(
        "poetry", "install", "--only", "static_type_checking", external=True
    )
    session.run("mypy", "src/")


@nox.session(python=["3.11"])
def lint(session):
    session.run("poetry", "install", "--only", "linting", external=True)
    session.run("flake8", "src/")


@nox.session(python=["3.11"])
def run_all_tests(session):
    session.run("poetry", "install", "--only", "testing", external=True)
    session.run("pytest")
