from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)



def test_get_jobs():
    expected_keys = ['job_location', 'job_role', 'salary', 'id']
    expected_keys.sort()
    response = client.get("/jobs")
    response_list = response.json()
    assert response.status_code == 200
    all_keys = [k for d in response_list for k in d.keys()]
    all_keys.sort()
    all_keys = list(dict.fromkeys(all_keys))
    assert  expected_keys == all_keys

def test_create_jobs():
    response = client.post(
        "/jobs/",
        json={
        "job_role": "android developer",
        "salary": 70000,
        "job_location": "chennai"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "job_role": "android developer",
            "salary": 70000,
            "job_location": "chennai",
            "id": response.json()['id']
            }

def test_apply_jobs():
    response = client.post(
        "/jobs/1/apply/1",
        json={
        "job_id": 3,
        "canditate_id": 1
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "job_id": 3,
            "canditate_id": 1,
            "id": response.json()['id']
            }

def test_get_canditates():
    expected_keys = ['name', 'email', 'id']
    expected_keys.sort()
    response = client.get("/canditates")
    response_list = response.json()
    assert response.status_code == 200
    all_keys = [k for d in response_list for k in d.keys()]
    all_keys.sort()
    all_keys = list(dict.fromkeys(all_keys))
    assert  expected_keys == all_keys



def test_get_jobs_based_on_id():
    expected_keys = ['job_role', 'salary', 'job_location', 'id']
    expected_keys.sort()
    response = client.get("/jobs/2")
    response_list = response.json()
    assert response.status_code == 200
    all_keys = list(response_list.keys())
    all_keys.sort()
    assert  expected_keys == all_keys

def test_applied_jobs():
    expected_keys = ['job_id', 'canditate_id', 'id']
    expected_keys.sort()
    response = client.get("/appliedjobs")
    response_list = response.json()
    assert response.status_code == 200
    all_keys = [k for d in response_list for k in d.keys()]
    all_keys.sort()
    all_keys = list(dict.fromkeys(all_keys))
    assert  expected_keys == all_keys

def test_delete_jobs():
    response = client.delete(
        "/jobs/9",
        json={
        "job_id": 9
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "message": "Deleted job_id 9"
            }


def test_create_canditates():
    response = client.post(
        "/canditates",
        json={
            "name": "farook",
            "email": "farookrceg@gmail.com"
            },
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "farook",
            "email": "farookrceg@gmail.com",
            "id": response.json()['id']
            }

