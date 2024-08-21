import json
import requests

# Set local Vars
GROUP_ID = "*****"
API_VERSION = "2024-08-15"
API_KEY = "*****"


def get_organizations(group_id, api_version, api_key):
  url = f"https://api.snyk.io/rest/groups/{group_id}/orgs?version={api_version}&limit=100"
  headers = {
      "accept": "application/vnd.api+json",
      "Authorization": f"{api_key}"
  }
  response = requests.get(url, headers=headers)
  response.raise_for_status()

  data = response.json()
  return data["data"]

def get_projects(org_id, api_version, api_key):
  url = f"https://api.snyk.io/rest/orgs/{org_id}/projects?version={api_version}&limit=100"
  headers = {
      "accept": "application/vnd.api+json",
      "Authorization": f"{api_key}"
  }
  response = requests.get(url, headers=headers)
  response.raise_for_status()

  data = response.json()
  return data["data"]

def extract_project_info(project, organizations):
  org_id = project["relationships"]["organization"]["data"]["id"]
  project_id = project["id"]
  status = project["attributes"]["status"]
  project_name = project["attributes"]["name"]
  type = project["attributes"]["type"]
  target_file = project["attributes"]["target_file"]
  
  # Find the organization in the organizations dictionary
  org_info = organizations.get(org_id)  

  # Handle potential case where org_id is not found
  if org_info is None:
      # Handle missing organization (e.g., log a warning)
      print(f"Warning: Organization with ID {org_id} not found")
      return None  # Or return a default value

  org_name = org_info["attributes"]["name"]

  return {"org_name": org_name, "org_id": org_id, "project_name": project_name, "project_id": project_id, "type": type, "target_file": target_file, "status": status}


def main():
  group_id = GROUP_ID
  api_version = API_VERSION 
  api_key = API_KEY

  # Get organizations and store them in a dictionary
  organizations = get_organizations(group_id, api_version, api_key)
  organizations_dict = {org["id"]: org for org in organizations}

  # Process organizations and projects
  project_data = []
  for organization in organizations:
    org_id = organization["id"]
    projects = get_projects(org_id, api_version, api_key)
    for project in projects:
      project_info = extract_project_info(project, organizations_dict)
      project_data.append(project_info)

  # Write project data to JSON file
  with open("project_data.json", "w") as outfile:
    json.dump(project_data, outfile, indent=4)

  print("Project data written to project_data.json")

if __name__ == "__main__":
  main()