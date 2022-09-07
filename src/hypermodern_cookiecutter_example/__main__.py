"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hypermodern Cookiecutter Example."""
    print("Hello World")
    print("This is an example of hypermodern package")


if __name__ == "__main__":
    main(prog_name="hypermodern-cookiecutter-example")  # pragma: no cover
