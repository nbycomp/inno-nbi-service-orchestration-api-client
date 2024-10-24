import unittest
from inno_nbi_api.models.block_args_deploy import BlockArgsDeploy
from inno_nbi_api.models.block_args_update import BlockArgsUpdate

class TestBlockArgs(unittest.TestCase):
    """BlockArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance_deploy(self, include_optional) -> BlockArgsDeploy:
        """Test BlockArgsDeploy"""
        if include_optional:
            return BlockArgsDeploy(
                site_id='34523423452345',
                display_name='Test Service 1',
                block_chart_name='Test Service 1',
                block_chart_version='0.0.1',
                values=''
            )
        else:
            return BlockArgsDeploy()

    def make_instance_update(self, include_optional) -> BlockArgsUpdate:
        """Test BlockArgsUpdate"""
        if include_optional:
            return BlockArgsUpdate(
                id='34523423452345',
                display_name='Test Service 1',
                block_chart_name='Test Service 1',
                block_chart_version='0.0.1',
                values=''
            )
        else:
            return BlockArgsUpdate()

    def testBlockArgsDeploy(self):
        """Test BlockArgsDeploy"""
        inst_req_only = self.make_instance_deploy(include_optional=False)
        self.assertIsInstance(inst_req_only, BlockArgsDeploy)

        inst_req_and_optional = self.make_instance_deploy(include_optional=True)
        self.assertIsInstance(inst_req_and_optional, BlockArgsDeploy)
        self.assertEqual(inst_req_and_optional.site_id, '34523423452345')
        self.assertEqual(inst_req_and_optional.display_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_version, '0.0.1')
        self.assertEqual(inst_req_and_optional.values, '')

    def testBlockArgsUpdate(self):
        """Test BlockArgsUpdate"""
        inst_req_only = self.make_instance_update(include_optional=False)
        self.assertIsInstance(inst_req_only, BlockArgsUpdate)

        inst_req_and_optional = self.make_instance_update(include_optional=True)
        self.assertIsInstance(inst_req_and_optional, BlockArgsUpdate)
        self.assertEqual(inst_req_and_optional.id, '34523423452345')
        self.assertEqual(inst_req_and_optional.display_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_version, '0.0.1')
        self.assertEqual(inst_req_and_optional.values, '')

if __name__ == '__main__':
    unittest.main()
