import unittest
from fastapi.testclient import TestClient
import logging
from main import app

logging.basicConfig(level=logging.DEBUG)
class DoLoginTestCase(unittest.TestCase):
    log=logging.getLogger(__name__)
    client = TestClient(app)
    def setUp(self) -> None:
        pass

    def test_something(self):
        self.log.debug("test_something")

        response = self.client.post("/token", headers={"Content-Type": "application/json"},

                                    json={"username": "admin", "password": "admin"})

        assert response.status_code == 200
        assert "access_token" in response.json().keys()


if __name__ == '__main__':
    unittest.main()
