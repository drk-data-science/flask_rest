from flask_script import Manager
from bucketlist.app import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
