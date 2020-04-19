from hmsc import db, app
import click
from hmsc.models import *


@app.cli.command()
@click.option('--drop',is_flag=True,help='先删除')
def init_db(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化完成')