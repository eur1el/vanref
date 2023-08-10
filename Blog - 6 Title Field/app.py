#imports website file and allows access to it, imports create app function
from website import create_app

#runs flask application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
