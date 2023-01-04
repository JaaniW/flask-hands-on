
class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = '12782jasdkjbasafdkjnasfoihasfbn317371##461264$$@21312312'
    FLASK_APP = 'FLASK_APP'
    FLASK_ENV = 'FLASK_ENV'

    # Database
    USER='postgres'
    PW='sajani95'
    DB='flask-handas-on'
    HOST='localhost'
    PORT='5433'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PW}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DEBUG=True