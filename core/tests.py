import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import Device


@pytest.fixture
def create_user(db, django_user_model):
    """Create a test user."""
    user = django_user_model.objects.create_user(
        username="testuser", email="teste@teste.com", password="testpassword"
    )
    return user


@pytest.fixture
def get_auth_token(create_user):
    """Obtain authentication token for the test user."""
    refresh = RefreshToken.for_user(create_user)
    return {"Authorization": f"Bearer {str(refresh.access_token)}"}


@pytest.fixture
def api_client():
    """Return an API client."""
    return APIClient()


@pytest.fixture
def create_device(create_user):
    """Create a sample device assigned to the test user."""
    return Device.objects.create(
        user=create_user, name="Test Device", ip="192.168.1.1", is_active=True
    )


def test_create_device(api_client, get_auth_token, create_user):
    """Test device creation endpoint."""

    url = reverse("devices")
    data = {
        "user": create_user.id,
        "name": "New Device",
        "ip": "192.168.1.2",
        "is_active": True,
    }
    response = api_client.post(url, data, format="json", headers=get_auth_token)

    assert response.status_code == 201
    assert response.data["name"] == "New Device"


def test_get_device_list(api_client, get_auth_token, create_device):
    """Test retrieving the device list."""
    url = reverse("devices")
    response = api_client.get(url, headers=get_auth_token)

    assert response.status_code == 200
    assert len(response.data) > 0


def test_should_not_show_list_device_from_other_user(api_client, create_device):
    """Test should return zero data"""
    user = User.objects.create_user(
        username="teste2", email="teste2@test2.com", password="teste2"
    )
    refresh = RefreshToken.for_user(user)
    token = {"Authorization": f"Bearer {str(refresh.access_token)}"}
    url = reverse("devices")
    response = api_client.get(url, headers=token)
    assert len(response.data) == 0


def test_should_return_error(api_client, create_device):
    """Test Should return error 401"""
    url = reverse("devices")
    response = api_client.get(url)
    assert response.data["message"] == "Hello, anonymous user!"
    assert response.status_code == 401
