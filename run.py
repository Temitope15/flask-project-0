# This file will run the application
from app import create_app

app = create_app() #to run the code in init.py

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)