from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)

# class Item(db.Model):
#     placement = db.Column(db.Integer(), primary_key=True)
#     placement1 = db.Column(db.Integer(), nullable=False)
#     placement2 = db.Column(db.Integer(), nullable=False)
#     placement3 = db.Column(db.Integer(), nullable=False)

#     def __repr__(self):
#         return f'Item {self.placement}'

# Use the Flask app context
# with app.app_context():
#     # Create the database tables
#     db.create_all()
#     item1 = Item(placement=1, placement1=10, placement2=20, placement3=30)
#     item2 = Item(placement=2, placement1=15, placement2=25, placement3=35)
#     item3 = Item(placement=3, placement1=12, placement2=22, placement3=32)
#     db.session.add_all([item1, item2, item3])
#     db.session.commit()

# Now you can query the items
# with app.app_context():
#     # Query all items from the Item table
#     items = Item.query.all()

#     # Print the results
#     for item in items:
#         print(f'Item {item.placement}: {item.placement1}, {item.placement2}, {item.placement3}')


# Create the database tables
# with app.app_context():
#     db.create_all()

# # Add data to the database
# with app.app_context():
#     item1 = Item(placement=1, placement1=10, placement2=20, placement3=30)
#     item2 = Item(placement=2, placement1=15, placement2=25, placement3=35)
#     item3 = Item(placement=3, placement1=12, placement2=22, placement3=32)

#     db.session.add_all([item1, item2, item3])

#     # Commit the changes to the database
#     db.session.commit()

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/college')
def college_page():
    items=[{
        'college':"IITB", 'placement':20000
    }]
    return render_template('college.html', items=items)
