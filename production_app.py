import os

from app import create_app
from config.app_config import ProductionConfig

if "SECRET_KEY" not in os.environ:
    raise Warning("The secret key must be passed by the <SECRET_KEY> env var.")

application = create_app(ProductionConfig)
