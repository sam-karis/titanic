
#! /usr/bin/python3
import click
from src.data.get_processed_data import read_data, processed_data, write_data_to_csv
from src.models.load_submit_data import load_model_scaler, get_submission_file

@click.group()
def cli():
    pass

@cli.command('download')
def download_data():
    click.echo('To download the data run the command below:')
    command = 'make download'
    click.echo('%s' %command)

@cli.command('process')
def process():
    click.echo("Reading raw data.....")
    df = read_data()
    click.echo("Processing data.....")
    df = processed_data(df)
    click.echo("Writing data to csv file.....")
    write_data_to_csv(df)
    click.echo("Done processed data is ready for modelling.")


@cli.command('make_submit')
@click.option('--filename', prompt='Enter file name to save prediction', help='Submission file name.')
def test(filename):
    click.echo("Loading model and scaler.....")
    model, scaler = load_model_scaler()
    click.echo("Making prediction on test data.....")
    filename = filename + '.csv'
    get_submission_file(model, filename, scaler)
    click.echo("Prediction ready submission on kaggle .....")


if __name__ == "__main__":
    cli()