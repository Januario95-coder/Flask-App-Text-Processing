import os 

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'd1620f453527ebb393a4f3574f2431437d9c6076a270ce1d686e23d73f71b3128887efa18fd6f418bd2ff387a4df4aeb28082678db5982a5ae0eb3f878716165'
    
    
    
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True