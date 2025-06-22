from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
