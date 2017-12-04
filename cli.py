import click


@click.group(chain=True)
def cli():
    pass


@cli.command('login')
@click.option('--username')
@click.option('--password')
def login(username,password):
    click.echo('Welcome ! '+username+"!")



@cli.command('register')
@click.argument('username')
@click.option('--password')
@click.option('--email')
def register(username,password,email):
    click.echo("Sucess "+username+","+password+","+email)


if __name__ == '__main__':
    cli()
