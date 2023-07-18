from flask import Flask, request, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy_serializer import SerializerMixin as SM
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user

db = SQLAlchemy()