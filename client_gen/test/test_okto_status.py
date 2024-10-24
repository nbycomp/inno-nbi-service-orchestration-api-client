import unittest
from inno_nbi_api.models.okto_status import OktoStatus

class TestOktoStatus(unittest.TestCase):
    """OktoStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OktoStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return {
                "status_code": OktoStatus.OKTOSTATUS_IN_SYNC,
                "message": "Everything is in sync"
            }
        else:
            return {
                "status_code": OktoStatus.OKTOSTATUS_IN_SYNC
            }

    def testOktoStatus_required_only(self):
        """Test OktoStatus with only required params"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertEqual(inst_req_only["status_code"], OktoStatus.OKTOSTATUS_IN_SYNC)
        self.assertNotIn("message", inst_req_only)

    def testOktoStatus_required_and_optional(self):
        """Test OktoStatus with required and optional params"""
        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional["status_code"], OktoStatus.OKTOSTATUS_IN_SYNC)
        self.assertEqual(inst_req_and_optional["message"], "Everything is in sync")

if __name__ == '__main__':
    unittest.main()
