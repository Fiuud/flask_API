# import json
# from tests import BaseTestCase
# from app.models import User
#
#
# class TestRoutes(BaseTestCase):
#     def test_get_users(self):
#         response = self.app.get('/users')
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(data['users']), 0)
#
#     def test_create_user(self):
#         data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
#         response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(data['user']['username'], 'testuser')
#
#     def test_get_user(self):
#         user = User(username='testuser', email='testuser@example.com')
#         user.set_password('testpassword')
#         self.db.session.add(user)
#         self.db.session.commit()
#
#         response = self.app.get('/users/{}'.format(user.id))
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(data['user']['username'], 'testuser')
#
#     def test_update_user(self):
#         user = User(username='testuser', email='testuser@example.com')
#         user.set_password('testpassword')
#         self.db.session.add(user)
#         self.db.session.commit()
#
#         data = {'username': 'newtestuser', 'email': 'newtestuser@example.com', 'password': 'newtestpassword'}
#         response = self.app.put('/users/{}'.format(user.id), data=json.dumps(data), content_type='application/json')
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(data['user']['username'], 'newtestuser')
#
#     def test_delete_user(self):
#         user = User(username='testuser', email='testuser@example.com')
#         user.set_password('testpassword')
#         self.db.session.add(user)
#         self.db.session.commit()
#
#         response = self.app.delete('/users/{}'.format(user.id))
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(data['message'], 'User deleted')
