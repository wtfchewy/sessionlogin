import os 

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "nischalNEEDSagirlfriend"
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

def format(number):
    return "-".join(number[i:i+4] for i in range(0, len(number), 4))