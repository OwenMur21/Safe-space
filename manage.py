from flask_script import Manager,Server
from app import create_app,db

app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Commentcrisis = Commentcrisis, Crisis = Crisis, Fam = Fam, Commentlines = Commentlines)
if __name__ == '__main__':
    manager.run()
