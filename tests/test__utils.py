import cjson
from .test_utils import TestCase

class ParamRequestHandlerTest(TestCase):
    def setUp(self):
        super(ParamRequestHandlerTest, self).setUp()
        self.url = "/testing/param_request"
        self.data = dict(int_param=1, float_param=2.5, str_param="bla", bool_param=True)
    def _request(self, data, **kwargs):
        return self.app.post(self.url, data=data, **kwargs)
    def test__json(self):
        r = self._request(cjson.encode(self.data), content_type="application/json")
        self.assertEquals(r.status_code, 200)
    def test__formdata(self):
        r = self._request(self.data)
        self.assertEquals(r.status_code, 200)
