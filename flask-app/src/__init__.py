# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'northwind'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add a default route
    @app.route("/")
    def welcome():
        return "<h1>Hello from the sublet apartment app team: Mia, Krina, Launna, and Jakob!</h1>"

    # Import the various routes
    from src.views import views
    from src.customers.customers import customers
    from src.products.products  import products
    from src.subletters.subletters import subletters
    from src.messages.messages import messages
    from src.posts.posts import posts

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views, url_prefix='/v')
    app.register_blueprint(customers, url_prefix='/c')
    app.register_blueprint(products, url_prefix='/pr')
    app.register_blueprint(subletters, url_prefix='/st')
    app.register_blueprint(messages, url_prefix='/m')
    app.register_blueprint(posts, url_prefix = '/po')

    return app