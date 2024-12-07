import os  # to be able to access the operating system of the system it is running on to be able to access env variables and file paths


class Config:

    # this will let me be able to work locally
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # if not SECRET_KEY:
    #     raise ValueError("SECRET_KEY is not set. Set it as an encironment variable.") this will hwlp e to be able to work on production

    # in the tutorial guide , i was to set a fallback value so that it can work locally even if anything is wrong, but on research i realised it is not a good practice, the secreet key should always be set, if not found, throw an error

    # to get the absolute path of this config file to ensure the app works regardless of where is is deployed
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', f'sqlite:///{os.path.join(basedir, "app.db")}')

    # this is to attach the url stored in the env file to the variable....there is a fallback that allows me to use it for local development

    # to reduce the additional load it causes
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
