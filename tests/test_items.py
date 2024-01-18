import unittest
from fastapi.testclient import TestClient
import logging
from main import app

logging.basicConfig(level=logging.DEBUG)
class ItemsTestCases(unittest.TestCase):
    log=logging.getLogger(__name__)
    client = TestClient(app)
    headers= {"Content-Type": "application/json"}
    def setUp(self) -> None:
        response = self.client.post("/token", headers={"Content-Type": "application/json"},json={"username": "admin", "password": "admin"})
        token=response.json().get("access_token")
        self.headers.update({"Authorization": f"Bearer {token}"})

    def test_create(self):
        response = self.client.post("/items/", headers=self.headers,json={"title": "Test Item", "description": "Testing items"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("title"), "Test Item")
    def test_list(self):
        response = self.client.get("/items/", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)






if __name__ == '__main__':
    unittest.main()
