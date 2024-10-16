import unittest
from inno_nbi_api.models.organization import Organization, DeviceMeta
from inno_nbi_api.models.device_meta import DeviceMeta

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        if include_optional:
            return Organization(
                id='123',
                display_name='Test Organization',
                description='A test organization',
                sites=['site1', 'site2'],
                device_metas=[
                    DeviceMeta(id='device1'),
                    DeviceMeta(id='device2')
                ]
            )
        else:
            return Organization()

    def testOrganization_required_only(self):
        """Test Organization with only required params"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertIsInstance(inst_req_only, Organization)
        self.assertIsNone(inst_req_only.id)
        self.assertIsNone(inst_req_only.display_name)
        self.assertIsNone(inst_req_only.description)
        self.assertIsNone(inst_req_only.sites)
        self.assertIsNone(inst_req_only.device_metas)

    def testOrganization_required_and_optional(self):
        """Test Organization with required and optional params"""
        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.id, '123')
        self.assertEqual(inst_req_and_optional.display_name, 'Test Organization')
        self.assertEqual(inst_req_and_optional.description, 'A test organization')
        self.assertEqual(inst_req_and_optional.sites, ['site1', 'site2'])
        self.assertEqual(len(inst_req_and_optional.device_metas), 2)
        self.assertEqual(inst_req_and_optional.device_metas[0].id, 'device1')
        self.assertEqual(inst_req_and_optional.device_metas[1].id, 'device2')

if __name__ == '__main__':
    unittest.main()
