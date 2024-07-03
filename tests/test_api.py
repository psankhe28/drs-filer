import requests
import json
import os

# Base URL
base_url = os.getenv('DRS_FILER_URL')


# Function to perform GET requests
def perform_get(endpoint):
    response = requests.get(base_url + endpoint, headers={'Accept': 'application/json'})
    return response.json()

# Function to perform POST requests
def perform_post(endpoint, data):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(base_url + endpoint, headers=headers, data=json.dumps(data))
    return response.json()

# Function to perform PUT requests
def perform_put(endpoint, data):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.put(base_url + endpoint, headers=headers, data=json.dumps(data))
    return response.json()

# Function to perform DELETE requests
def perform_delete(endpoint):
    response = requests.delete(base_url + endpoint, headers={'Accept': 'application/json'})
    return response.json()

# Test cases
if __name__ == '__main__':
    try:
        # Test GET /service-info
        print("GET /service-info:")
        print(perform_get('service-info'))

        # Test GET /objects
        print("\nGET /objects:")
        print(perform_get('objects'))

        # Test POST /objects
        print("\nPOST /objects:")
        create_object_data = {
            "access_methods": [
                {
                    "access_url": {
                        "headers": [],
                        "url": "http://example.com/data"
                    },
                    "region": "us-east-1",
                    "type": "s3"
                }
            ],
            "aliases": ["example_alias"],
            "checksums": [
                {
                    "checksum": "abc123",
                    "type": "sha-256"
                }
            ],
            "contents": [],
            "created_time": "2024-06-12T12:58:19Z",
            "description": "An example object",
            "mime_type": "application/json",
            "name": "example_object",
            "size": 1024,
            "updated_time": "2024-06-12T12:58:19Z",
            "version": "1.0"
        }
        response = perform_post('objects', create_object_data)
        object_id = response.get('id')
        print(response)

        # Test GET /objects/{object_id}
        print(f"\nGET /objects/{object_id}:")
        response = perform_get(f'objects/{object_id}')
        access_id = response['access_methods'][0]['access_id']
        print(response)

        # Test GET /objects/{object_id}/access/{access_id}
        print(f"\nGET /objects/{object_id}/access/{access_id}:")
        response = perform_get(f'objects/{object_id}/access/{access_id}')
        print(response)

        # Test PUT /objects/{object_id}
        print(f"\nPUT /objects/{object_id}:")
        put_data = {
            "access_methods": [
                {
                    "access_url": {
                        "headers": ["string"],
                        "url": "string"
                    },
                    "region": "us-east-1",
                    "type": "s3"
                }
            ],
            "aliases": ["string"],
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
        response = perform_put(f'objects/{object_id}', put_data)
        print(response)

        # Test DELETE /objects/{object_id}/access/{access_id}
        print(f"\nDELETE /objects/{object_id}/access/{access_id}:")
        response = perform_delete(f'objects/{object_id}/access/{access_id}')
        print(response)

        # Test DELETE /objects/{object_id}
        print(f"\nDELETE /objects/{object_id}:")
        response = perform_delete(f'objects/{object_id}')
        print(response)

        # Test POST /service-info
        print("\nPOST /service-info:")
        service_info_data = {
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
        response = perform_post('service-info', service_info_data)
        print(response)

        # Test GET /service-info again
        print("\nGET /service-info:")
        print(perform_get('service-info'))

    except Exception as e:
        print(f"Error occurred: {str(e)}")
