import os
from dotenv import load_dotenv

# Load environment variables FIRST
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

from app import create_app

# Create the app instance so the FLASK_APP system can find it
app = create_app()


# This block is only for running the development server directly
if __name__ == '__main__':
    app.run(debug=True, port=5001)