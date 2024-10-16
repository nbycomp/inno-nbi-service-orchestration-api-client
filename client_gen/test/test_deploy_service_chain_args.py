import unittest
from inno_nbi_api.models.deploy_service_chain_args import DeployServiceChainArgs
from inno_nbi_api.models.block_args_deploy import BlockArgsDeploy

class TestDeployServiceChainArgs(unittest.TestCase):
    """DeployServiceChainArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeployServiceChainArgs:
        """Test DeployServiceChainArgs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return DeployServiceChainArgs(
                name='test_name',
                blocks=[
                    BlockArgsDeploy(
                        site_id='12342-23423984-234-234234',
                        display_name='Test Block',
                        block_chart_name='test_chart',
                        block_chart_version='1.0',
                    )
                ]
            )
        else:
            return DeployServiceChainArgs(
                name='test_name'
            )

    def testDeployServiceChainArgs(self):
        """Test DeployServiceChainArgs"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertEqual(inst_req_only.name, 'test_name')
        self.assertIsNone(inst_req_only.blocks)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.name, 'test_name')
        self.assertIsNotNone(inst_req_and_optional.blocks)
        self.assertEqual(inst_req_and_optional.blocks[0].site_id, '12342-23423984-234-234234')
        self.assertEqual(inst_req_and_optional.blocks[0].display_name, 'Test Block')
        self.assertEqual(inst_req_and_optional.blocks[0].block_chart_name, 'test_chart')
        self.assertEqual(inst_req_and_optional.blocks[0].block_chart_version, '1.0')

if __name__ == '__main__':
    unittest.main()
