Titanic
==============================

Create a model to predict survival of individuals in the titanic ship


To download the data .  
- Create account at kaggle
- To use kaggle api first install it `pip install kaggle`
- To use this api sign in at [kaggle](https://www.kaggle.com) the go Account tab and slect **Create API Token** this will generate for you a file `kaggle.json` place it in the project root directory.
- Run this command `kaggle competitions download  -c titanic -p data/raw/` or go to the notebook named `download_data` and run the cell to download the titanic datasets.   

To view data exploration and processing go to `notebooks\explore_process_data`. Here one get basic understanding of the data structure of titanic dataset and very interesting properties about the data.   
To automatically process and save the processed data that will be used for modelling run `python manage.py process`   
To view defination and training of various model go to `notebooks\predictive_model`. Here I define the following:-
- Baseline model  
- Basic linear regression model
- Optimize model parameters
- Model Persistence   

To automatically load saved model, make predictions and save them in a `csv` file run `python manage.py make_submit`


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── predict_model.py
    │       └── train_model.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
