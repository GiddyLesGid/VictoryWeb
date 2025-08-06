# migrate_setup.py
from app import app
from models import db  # Make sure db = SQLAlchemy() is in models.py
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    from flask.cli import main
    main()
