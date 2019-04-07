from app import app
# db config
from app import config
# admin and site view importation
from app import views
from app import admin_views

if __name__ == '__main__':
    app.run(debug=True)
