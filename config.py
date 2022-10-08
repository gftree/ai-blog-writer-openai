
import os

##OPEN API STUFF
#OPENAI_API_KEY = 'enter-api-key'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
