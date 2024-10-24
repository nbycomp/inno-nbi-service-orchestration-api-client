import unittest
from inno_nbi_api.models.update_service_chain_args import UpdateServiceChainArgs
from inno_nbi_api.models.block_args_update import BlockArgsUpdate

class TestUpdateServiceChainArgs(unittest.TestCase):
    """UpdateServiceChainArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateServiceChainArgs:
        """Test UpdateServiceChainArgs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return UpdateServiceChainArgs(
                id='service_chain_1',
                name='Updated Service Chain',
                blocks=[
                    BlockArgsUpdate(
                        id='block1',
                        display_name='Block 1',
                        block_chart_name='block_chart_1',
                        block_chart_version='v1',
                        values='some_values'
                    )
                ]
            )
        else:
            return UpdateServiceChainArgs(
                id='service_chain_1',
                name='Updated Service Chain'
            )

    def testUpdateServiceChainArgs_required_only(self):
        """Test UpdateServiceChainArgs with only required params"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertIsInstance(inst_req_only, UpdateServiceChainArgs)
        self.assertEqual(inst_req_only.id, 'service_chain_1')
        self.assertEqual(inst_req_only.name, 'Updated Service Chain')
        self.assertIsNone(inst_req_only.blocks)

    def testUpdateServiceChainArgs_required_and_optional(self):
        """Test UpdateServiceChainArgs with required and optional params"""
        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertIsInstance(inst_req_and_optional, UpdateServiceChainArgs)
        self.assertEqual(inst_req_and_optional.id, 'service_chain_1')
        self.assertEqual(inst_req_and_optional.name, 'Updated Service Chain')
        self.assertIsNotNone(inst_req_and_optional.blocks)
        self.assertEqual(len(inst_req_and_optional.blocks), 1)
        self.assertEqual(inst_req_and_optional.blocks[0].id, 'block1')
        self.assertEqual(inst_req_and_optional.blocks[0].display_name, 'Block 1')
        self.assertEqual(inst_req_and_optional.blocks[0].block_chart_name, 'block_chart_1')
        self.assertEqual(inst_req_and_optional.blocks[0].block_chart_version, 'v1')
        self.assertEqual(inst_req_and_optional.blocks[0].values, 'some_values')

if __name__ == '__main__':
    unittest.main()
