import nox


@nox.session(python=["3.11"])
def test(session):
    session.run("poetry", "install", "--only", "test", external=True)
    session.run("pytest")


@nox.session(python=["3.11"])
def format(session):
    session.run("poetry", "install", "--only", "format", external=True)
    session.run("black", ".")


@nox.session(python=["3.11"])
def lint(session):
    session.run("poetry", "install", "--only", "lint", external=True)
    session.run("flake8", "src/")


@nox.session(python=["3.11"])
def static_type_check(session):
    session.run(
        "poetry", "install", "--only", "static_type_check", external=True
    )
    session.run("mypy", "src/")
