from .app import app
from .utils import param_request_handler
from flask import make_response

@app.route("/testing/param_request", methods=["POST"])
@param_request_handler(int_param=int, float_param=float, str_param=str, bool_param=bool)
def test__param_request(int_param, float_param, str_param, bool_param):
    assert isinstance(int_param, int)
    assert isinstance(float_param, float)
    assert isinstance(bool_param, bool)
    assert isinstance(str_param, str)
    return make_response("ok")
