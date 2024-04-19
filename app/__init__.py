from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os


# callable wsgi-приложение
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/george/learning/projects/adventurer/database.db' # + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключение отслеживания модификаций

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models

# # Необходимо добавить путь к моделям в PYTHONPATH
# import sys
# sys.path.insert(0, os.getcwd())  # Добавление текущего каталога в путь поиска
# from models import *  # Импорт всех моделей из вашего приложения

# # Подключение моделей к миграционному контексту
# target_metadata = db.metadata