# job_portal_fast_api

# get all jobs

method: get

end url: http://127.0.0.1:8000/jobs/

# create jobs

method: post

end url: /jobs

request body: {
  "job_role": "string",
  "salary": int,
  "job_location": "string"
}

# Delete jobs based on id

method: delete

end url: /jobs/{job_id}

# get job by id

method: get

end url: http://127.0.0.1:8000/jobs/2

# apply job based on id

method: post

end url: /jobs/{job_id}/apply

params: {job_id}

request params: {
  "name": "string",
  "email": "string"
}

# view applied jobs

method: get

end url: http://127.0.0.1:8000/appliedjobs/




