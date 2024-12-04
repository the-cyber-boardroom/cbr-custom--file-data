from unittest                                      import TestCase
from cbr_custom_file_data.utils.Version           import version__cbr_custom_file_data
from tests.integration.file_data__objs_for_tests  import file_data__fast_api__client


class test__client__Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = file_data__fast_api__client

    def test_raw__uk__homepage(self):
        response = self.client.get('/info/version')
        assert response.status_code == 200
        assert response.json()      == {'version': version__cbr_custom_file_data }

