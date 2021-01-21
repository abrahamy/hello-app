from os import nice
import pytest
from hello_app.services import address_parser


@pytest.mark.parametrize(
    "address,expected",
    [
        ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
        ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
        ("Am Bächle 23", {"street": "Am Bächle", "housenumber": "23"}),
        ("Auf der Vogelwiese 23 b", {"street": "Auf der Vogelwiese", "housenumber": "23 b"}),
        ("4, rue de la revolution", {"street": "rue de la revolution", "housenumber": "4"}),
        ("200 Broadway Av", {"street": "Broadway Av", "housenumber": "200"}),
        ("Calle Aduana, 29", {"street": "Calle Aduana", "housenumber": "29"}),
        ("Calle 39 No 1540", {"street": "Calle 39", "housenumber": "No 1540"}),
    ],
)
def test_address_parser(address: str, expected: dict) -> None:
    actual = address_parser.parse(address)
    assert actual == expected


@pytest.mark.parametrize("invalid_address", ["123456", 123456, None])
def test_address_parser_returns_parse_error_on_invalid_input(invalid_address):
    with pytest.raises(address_parser.ParseError):
        address_parser.parse(invalid_address)


def test_endpoint_returns_correct_result(client):
    payload = {"address": "Winterallee 3"}
    expected = {"street": "Winterallee", "housenumber": "3"}
    response = client.get("/api/address/", data=payload, content_type="application/json")
    assert response.status_code == 200
    assert response.data == expected


@pytest.fixture(scope="function")
def params(request, client):
    return request.param, client


@pytest.mark.parametrize("params", [{"address": ""}, None], indirect=True)
def test_endpoint_returns_400_on_empty_data(params):
    payload, client = params
    response = client.get("/api/address/", data=payload, content_type="application/json")
    assert response.status_code == 400


def test_endpoint_returns_400_on_invalid_data(client):
    payload = {"address": "123456"}
    response = client.get("/api/address/", data=payload, content_type="application/json")
    assert response.status_code == 422
