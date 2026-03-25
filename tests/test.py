import object_data


def test_get_objects(get_object_endpoint, api_headers):
    get_object_endpoint.get_objects(api_headers)
    get_object_endpoint.check_status_code_200()


def test_get_one(get_one_object_endpoint, api_headers):
    get_one_object_endpoint.get_object_by_id(api_headers, 1)
    get_one_object_endpoint.check_status_code_200()
    get_one_object_endpoint.check_body_response(object_data.body_object_id_1)

