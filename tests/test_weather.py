
from unittest.mock import patch, Mock

from src.weather import get_coordinates


def test_get_coordinates():
    # Simulate the API response
    mock_response = Mock()

    mock_response.json.return_value = {
        "results": [
            {
                "latitude": 23.3441,
                "longitude": 85.3096
            }
        ]
    }

    # Replace requests.get with our simulated response
    with patch("src.weather.requests.get", return_value=mock_response):
        latitude, longitude = get_coordinates("Ranchi")

    # Verify the output
    assert latitude == 23.3441
    assert longitude == 85.3096
