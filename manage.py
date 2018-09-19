from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Crisis, Commentcrisis, Fam, Commentfam, Health, Commenthealth,Mental,Commentmental
from  flask_migrate import Migrate, MigrateCommand



app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Commentcrisis = Commentcrisis, Crisis = Crisis, Fam = Fam, Commentfam = Commentfam,Health=Health,Commenthealth=Commenthealth,Mental=Mental,Commentmental=Commentmental)
if __name__ == '__main__':
    manager.run()
