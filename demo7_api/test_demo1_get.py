import requests
from assertpy import assert_that


class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"

    def test_find_valid_pet_by_id(self):
        pet_id = 1
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)

    def test_find_invalid_pet_by_id(self):
        pet_id = 2001
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(404).is_equal_to(response.status_code)
        assert_that("Pet not found").is_equal_to(response.json()["message"])
        print(response.json())

    def test_find_pet_by_valid_status(self):
        status = "sold"
        resource = f"/pet/findByStatus?status={status}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)
        for i in range(0, len(response.json())):
            assert_that(status).is_equal_to(response.json()[i]["status"])

    def test_find_pet_by_invalid_status(self):
        status = "sold123"
        resource = f"/pet/findByStatus?status={status}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(400).is_equal_to(response.status_code)