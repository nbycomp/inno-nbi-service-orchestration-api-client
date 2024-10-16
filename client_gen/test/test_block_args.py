import unittest
from inno_nbi_api.models.block_args import BlockArgs

class TestBlockArgs(unittest.TestCase):
    """BlockArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockArgs:
        """Test BlockArgs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        model = BlockArgs()
        if include_optional:
            return BlockArgs(
                id='34523423452345',
                display_name='Test Service 1',
                block_chart_name='Test Service 1',
                block_chart_version='0.0.1',
                values=''
            )
        else:
            return BlockArgs()

    def testBlockArgs(self):
        """Test BlockArgs"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertIsInstance(inst_req_only, BlockArgs)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertIsInstance(inst_req_and_optional, BlockArgs)
        self.assertEqual(inst_req_and_optional.id, '34523423452345')
        self.assertEqual(inst_req_and_optional.display_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_name, 'Test Service 1')
        self.assertEqual(inst_req_and_optional.block_chart_version, '0.0.1')
        self.assertEqual(inst_req_and_optional.values, '')

if __name__ == '__main__':
    unittest.main()
