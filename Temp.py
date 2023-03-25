import shotgun_api3

# Replace the values below with your own API key and script name
SERVER_PATH = 'https://moonshine.shotgunstudio.com/'
SCRIPT_NAME = 'easylife122'
API_KEY = 'iqnor4Bifz-gjswpvpliwjpxt'

# Create a connection to the Shotgrid API
sg = shotgun_api3.Shotgun(SERVER_PATH, script_name=SCRIPT_NAME, api_key=API_KEY)

# Fetch a list of all the shots in the project
# projects = sg.find('Project', [], ['name'])

project_id = 4082

_filter = [['project', 'is', {'id': project_id, 'type': 'Project'}], ['sg_status_list', 'is_not', 'omt']]
data = sg.find('Shot', _filter, ['id', 'code', 'sg_asset_type'])

print(data)