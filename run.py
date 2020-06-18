from app import create_app
from app.extension import db
from app.models import *
from config.app_config import LocalConfig
from constants.local_run import RUN_SETTING

app = create_app(LocalConfig)

if __name__ == "__main__":
    db.create_all(app=app)
    app.run(**RUN_SETTING)
