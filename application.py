"""
Entry point for AWS Elastic Beanstalk
"""
from app import app

# Elastic Beanstalk expects the application object to be named 'application'
application = app

if __name__ == '__main__':
    application.run()
