"""Tests to confirm that the Test Server conforms to the Test Runner specification for integration testing."""

import os
import json
import unittest

# Unit under test
from tests.integration.server import app


class EndpointTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup standard test client for flask apps"""
        cls.app = app.test_client()

        # When run locally this will use the default environment variables, when running in CI use the OS2
        # defaults for this test as it contacts the API to list the user entity.
        sdk_config = {}
        try:
            sdk_config["api_key"] = os.environ['TEST_RUNNER_DEFAULT_API_KEY']
        except KeyError:
            pass

        try:
            sdk_config["host"] = os.environ['TEST_RUNNER_DEFAULT_API_HOST']
        except KeyError:
            pass

        cls.sdk_config = json.dumps(sdk_config)

    def create_instance(self, url):
        """Create a module, entity or SDK instance."""
        return self.app.post(url, data=self.sdk_config, content_type='application/json')

    def test_ping(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_reset(self):
        response = self.app.post('/reset')
        self.assertEqual(response.status_code, 205)

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
        response = self.create_instance('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 201)
        instance_id = response.json["id"]
        response = self.app.get('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count + 1, "Created instance should be in the list.")

        # Delete created instance
        response = self.app.delete('/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 200)

        # Check instance has been deleted from the list
        response = self.app.get('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count, "Instance should not be in the list.")

    def test_unknown_module(self):
        module = "unknown"

        # Attempt to create an instance for a module that doesn't exist
        response = self.create_instance('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 404)

    def test_module_methods(self):
        module = "update"

        # Create a new instance
        response = self.create_instance('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 201)
        instance_id = response.json["id"]

        # Check methods can be listed
        response = self.app.get('/instances/%s/methods' % instance_id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

    def test_entities(self):
        response = self.app.get('/foundation/entities')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

    def test_entity_methods(self):
        entity = "User"

        # Create a new instance
        response = self.create_instance('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 201)
        instance_id = response.json["id"]

        # Check methods can be listed
        response = self.app.get('/foundation/instances/%s/methods' % instance_id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

        response = self.app.post('/foundation/instances/%s/methods/list' % instance_id)
        self.assertEqual(response.status_code, 200, str(response.json))

        response = self.app.post('/foundation/instances/%s/methods/unknown' % instance_id)
        self.assertEqual(response.status_code, 404)

    def test_sdk_methods(self):
        # Create a new instance
        response = self.create_instance('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 201)
        instance_id = response.json["id"]

        # Check methods can be listed
        response = self.app.get('/foundation/instances/%s/methods' % instance_id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

        # SDK methods should not be executable
        response = self.app.post('/foundation/instances/%s/methods/entities' % instance_id)
        self.assertEqual(response.status_code, 405)

    def test_sdk_instances(self):
        # Get a list of instances that already exist
        response = self.app.get('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 200)
        starting_instance_count = len(response.json)

        # Create a new instance
        response = self.create_instance('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 201)
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
        response = self.create_instance('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 201)
        instance_id = response.json["id"]
        response = self.app.get('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count + 1, "Created instance should be in the list.")

        # Delete created instance
        response = self.app.delete('/foundation/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 204)

        # Check instance has been deleted from the list
        response = self.app.get('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), starting_instance_count, "Instance should not be in the list.")

    def test_unknown_entity(self):
        entity = "unknown"

        # Attempt to create an instance for an entity that doesn't exist
        response = self.create_instance('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 404)

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
        response = self.create_instance('/foundation/sdk/instances')
        self.assertEqual(response.status_code, 201)
        # Create a new Foundation entity instance
        response = self.create_instance('/foundation/entities/%s/instances' % entity)
        self.assertEqual(response.status_code, 201)
        # Create a new module instance
        response = self.create_instance('/modules/%s/instances' % module)
        self.assertEqual(response.status_code, 201)

        # The instance list endpoint for foundation should not include module instances
        response = self.app.get('/foundation/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), foundation_instance_count + 2, "There should be two additional instances.")

        # The instance list endpoint for modules should not include foundation instances
        response = self.app.get('/instances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), module_instance_count + 1, "There should be one additional instance.")

    def test_unknown_foundation_instance(self):
        instance_id = "unknown"

        # Attempt to get an instance for a foundation entity that doesn't exist
        response = self.app.get('/foundation/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 404)

    def test_unknown_module_instance(self):
        instance_id = "unknown"

        # Attempt to get an instance for a foundation entity that doesn't exist
        response = self.app.get('/instances/%s' % instance_id)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
