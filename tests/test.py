import os
import requests

DRS_FILER_URL = os.getenv('DRS_FILER_URL')
    
def test_create_object():
    data = {
        "access_methods": [
            {
                "access_url": {
                    "url": "http://example.com/data"
                },
                "region": "us-east-1",
                "type": "s3"
            }
        ],
        "aliases": [
            "example_alias"
        ],
        "checksums": [
            {
                "checksum": "abc123",
                "type": "sha-256"
            }
        ],
        "name": "example_object",
        "size": 1024
    }
    response = requests.post(f"{DRS_FILER_URL}/objects", json=data)
    assert response.status_code == 200
    object_id = response.json()['id']
    print(f"Created object with ID: {object_id}")
    return object_id

    
def test_get_objects():
    response = requests.get(f"{DRS_FILER_URL}/objects")
    assert response.status_code == 200
    print(response.json())

def test_get_object(object_id):
    response = requests.get(f"{DRS_FILER_URL}/objects/{object_id}")
    assert response.status_code == 200
    print(response.json())

def test_get_object_access(object_id, access_id):
    response = requests.get(f"{DRS_FILER_URL}/objects/{object_id}/access/{access_id}")
    assert response.status_code == 200
    print(response.json())

def test_update_object(object_id):
    data = {
        "access_methods": [
            {
                "access_url": {
                    "headers": [
                        "string"
                    ],
                    "url": "string"
                },
                "region": "us-east-1",
                "type": "s3"
            }
        ],
        "aliases": [
            "string"
        ],
        "checksums": [
            {
                "checksum": "string",
                "type": "sha-256"
            }
        ],
        "contents": [
            {
                "contents": [],
                "drs_uri": [
                    "drs://drs.example.org/314159",
                    "drs://drs.example.org/213512",
                    "drs://drs.example.org/213516"
                ],
                "id": "string",
                "name": "string"
            }
        ],
        "created_time": "2024-06-12T06:27:29.248Z",
        "description": "string",
        "mime_type": "application/json",
        "name": "string",
        "size": 0,
        "updated_time": "2024-06-12T06:27:29.248Z",
        "version": "string"
    }
    response = requests.put(f"{DRS_FILER_URL}/objects/{object_id}", json=data)
    assert response.status_code == 200
    print(response.json())

def test_delete_object_access(object_id, access_id):
    response = requests.delete(f"{DRS_FILER_URL}/objects/{object_id}/access/{access_id}")
    assert response.status_code == 200
    print(response.json())
    
def test_delete_object(object_id):
    response = requests.delete(f"{DRS_FILER_URL}/objects/{object_id}")
    assert response.status_code == 200

def test_post_service_info():
    data = {
        "contactUrl": "mailto:support@example.com",
        "createdAt": "2024-06-12T12:58:19Z",
        "description": "This service provides...",
        "documentationUrl": "https://docs.myservice.example.com",
        "environment": "test",
        "id": "org.ga4gh.myservice",
        "name": "My project",
        "organization": {
            "name": "My organization",
            "url": "https://example.com"
        },
        "type": {
            "artifact": "beacon",
            "group": "org.ga4gh",
            "version": "1.0.0"
        },
        "updatedAt": "2024-06-12T12:58:19Z",
        "version": "1.0.0"
    }
    response = requests.post(f"{DRS_FILER_URL}/service-info", json=data)
    assert response.status_code == 200
    print(response.json())

def test_get_service_info():
    response = requests.get(f"{DRS_FILER_URL}/service-info")
    assert response.status_code == 200
    print(response.json())