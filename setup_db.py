from src import app, db

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database created!")
