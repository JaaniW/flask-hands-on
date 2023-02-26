class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "12782jasdkjbasafdkjnasfoihasfbn317371##461264$$@21312312"
    FLASK_APP = "FLASK_APP"
    FLASK_ENV = "FLASK_ENV"

    # Database
    USER = "postgres"
    PW = "sajani95"
    DB = "flask-handas-on"
    HOST = "localhost"
    PORT = "5433"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PW}@{HOST}:{PORT}/{DB}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "126#12312*^YHksajhgsagytu173uyibkajnsfoiugasvd"
    JWT_ACCESS_TOKEN_EXPIRES = 3600 * 24

    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'

    # DEBUG=True
