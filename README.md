# Bulk Activate / Deactivate Snyk Projects

De / activates projects across multiple Snyk Organisations in a Group.

## Features

`get_projects.py` - gathers project information for entire Snyk Orgnisation. Uses [Snyk's REST API](https://apidocs.snyk.io/).

`change_project_status.py` - De / activates selected projects. Uses [Snyk's V1 API](https://snyk.docs.apiary.io/).

## Configuration

Install dependencies
```sh
pip install -r requirements.txt
```

Update variables in `get_projects.py`. Get the latest API Version from [Snyk's REST API](https://apidocs.snyk.io/)
```py
GROUP_ID = "******"
API_VERSION = "2024-08-15"
API_KEY = "*****"
```

## Usage

### Gather project information 

Run the script locally

```sh
python3 get_projects.py
```

Script will output `project_data.json` file. Edit the file as necessary.


### Activate / Deactivate Projects

```sh
python3 change_proj_status.py project_data.json --action activate/deactivate --api_key your_api_key
```
