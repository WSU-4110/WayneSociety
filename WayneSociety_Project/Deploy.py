from flask_login import current_user
from flask import Blueprint
from flask import render_template, redirect
from flask import url_for, request
from flask import flash
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User
from .import db
import uuid

