from app import app, db
import unittest
from app.models import Dog, Slave

class TestDogModel(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_create_dogo(self):
        dogo = Dog('fluffy', 'pug', 2)

        self.assertEqual(len(Dog.query.all()), 0)

        db.session.add(dogo)
        db.session.commit()

        self.assertEqual(len(Dog.query.all()), 1)

        slv = Slave('male', 2)

        self.assertEqual(len(Slave.query.all()), 0)

        db.session.add(slv)
        db.session.commit()

        self.assertEqual(len(Slave.query.all()), 1)
        
if __name__  == '__main__':
    unittest.main()
