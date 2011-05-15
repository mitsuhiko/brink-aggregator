from flaskext.script import Manager
import brink

manager = Manager(brink.app)


@manager.command
def initdb():
    """Create the database tables"""
    print 'Using database %s' % brink.db.engine.url
    brink.db.create_all()
    print 'Created tables'


@manager.command
def sync():
    """Download new messages from twitter and forums"""
    brink.sync()
    print 'Done syncing'


if __name__ == '__main__':
    manager.run()
