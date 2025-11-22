import click
from generator_xss import XSSGenerator
from generator_sqli import SQLiGenerator
from encoder import Encoder
from mutate import Mutator


@click.group()
def cli():
    """Payload Generator CLI"""
    pass


# --------------------------------------
# LIST COMMAND
# --------------------------------------
@cli.command()
@click.option("--type", required=True, help="xss or sqli")
def list(type):
    if type == "xss":
        g = XSSGenerator()
        click.echo("\nAvailable XSS Payloads:")
        for p in g.list_ids():
            click.echo(f" - {p}")
    elif type == "sqli":
        g = SQLiGenerator()
        click.echo("\nAvailable SQLi Payloads:")
        for p in g.list_ids():
            click.echo(f" - {p}")
    else:
        click.echo("Invalid type!")


# --------------------------------------
# GENERATE PAYLOAD
# --------------------------------------
@cli.command()
@click.option("--id", required=True)
def generate(id):
    g1 = XSSGenerator()
    g2 = SQLiGenerator()

    payload = g1.generate_by_id(id) or g2.generate_by_id(id)

    click.echo("\nGenerated Payload:\n", nl=False)
    click.echo(payload)


# --------------------------------------
# ENCODER
# --------------------------------------
@cli.command()
@click.option("--method", required=True, type=click.Choice(["base64", "url", "html", "hex", "reverse", "wrap"]))
@click.option("--payload", required=True)
def encode(method, payload):
    e = Encoder()

    if method == "base64":
        out = e.base64_encode(payload)
    elif method == "url":
        out = e.url_encode(payload)
    elif method == "html":
        out = e.html_encode(payload)
    elif method == "hex":
        out = e.hex_encode(payload)
    elif method == "reverse":
        out = e.reverse(payload)
    elif method == "wrap":
        out = e.wrap(payload, "<<WRAP>>[[VALUE]]<<END>>")

    click.echo("\nEncoded Payload:\n")
    click.echo(out)


# --------------------------------------
# MUTATION MODULE
# --------------------------------------
@cli.group()
def mutate():
    """Mutate payloads"""
    pass


@mutate.command()
@click.option("--method", required=True, type=click.Choice(["case-flip", "reverse", "shuffle", "inject-null"]))
@click.option("--payload", required=True)
def run(method, payload):
    m = Mutator()

    if method == "case-flip":
        out = m.case_flip(payload)
    elif method == "reverse":
        out = m.reverse(payload)
    elif method == "shuffle":
        out = m.shuffle(payload)
    elif method == "inject-null":
        out = m.inject_null(payload)

    click.echo("\nMutated Payload:\n")
    click.echo(out)



if __name__ == "__main__":
    cli()
