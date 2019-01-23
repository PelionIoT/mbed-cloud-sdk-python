
import unittest

# Unit under test
from server import app


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_ping(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_modules(self):
        response = self.app.get('/modules')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

    def test_module_instances(self):
        module = "update"

        # Get a list of instances that already exist
        response = self.app.get('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        starting_instance_count = len(response.json)

        # Create a new instance
        response = self.app.post('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        instance_id = response.json["id"]
        response = self.app.get('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count+1, "Created instance should be in the list.")

        # Delete created instance
        response = self.app.delete('/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 200)

        # Check instance has been deleted from the list
        response = self.app.get('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count, "Instance should not be in the list.")

    def test_entities(self):
        response = self.app.get('/foundation/entities')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

    def test_sdk_instances(self):
        # Get a list of instances that already exist
        response = self.app.get('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        starting_instance_count = len(response.json)

        # Create a new instance
        response = self.app.post('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        instance_id = response.json["id"]
        response = self.app.get('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count + 1, "Created instance should be in the list.")

        # Delete created instance
        response = self.app.delete('/foundation/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 204)

        # Check instance has been deleted from the list
        response = self.app.get('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count, "Instance should not be in the list.")

    def test_entity_instances(self):
        entity = "User"

        # Get a list of instances that already exist
        response = self.app.get('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        starting_instance_count = len(response.json)

        # Create a new instance
        response = self.app.post('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        instance_id = response.json["id"]
        response = self.app.get('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count+1, "Created instance should be in the list.")

        # Delete created instance
        response = self.app.delete('/foundation/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 204)

        # Check instance has been deleted from the list
        response = self.app.get('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count, "Instance should not be in the list.")

    def test_instances_listing(self):
        """Test that the instance list endpoint only list appropriate entities."""
        entity = "User"
        module = "update"

        response = self.app.get('/foundation/instances')
        self.assertEqual(response.status_code, 200)
        foundation_instance_count = len(response.json)

        response = self.app.get('/instances')
        self.assertEqual(response.status_code, 200)
        module_instance_count = len(response.json)

        # Create a new top level SDK instance
        response = self.app.post('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        # Create a new Foundation entity instance
        response = self.app.post('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        # Create a new module instance
        response = self.app.post('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)

        # The instance list endpoint for foundation should not include module instances
        response = self.app.get('/foundation/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), foundation_instance_count + 2, "There should be two additional instances.")

        # The instance list endpoint for modules should not include foundation instances
        response = self.app.get('/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), module_instance_count + 1, "There should be one additional instance.")


if __name__ == "__main__":
    unittest.main()