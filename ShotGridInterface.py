import shotgun_api3

class shotgridQuery():
    def __init__(self):
        super().__init__()

        self.projects = []

        # Replace the values below with your own API key and script name
        SERVER_PATH = 'https://moonshine.shotgunstudio.com/'
        SCRIPT_NAME = 'easylife122'
        API_KEY = 'iqnor4Bifz-gjswpvpliwjpxt'

        # Create a connection to the Shotgrid API
        self.sg = shotgun_api3.Shotgun(SERVER_PATH, script_name=SCRIPT_NAME, api_key=API_KEY)

    def shotgridProject(self):

        # Fetch a list of all projects
        self.projects = self.sg.find('Project', [], ['name', 'id'])

        return self.projects

    def shotgridData(self, project_id):

        #Add a filter
        _filter = [['project', 'is', {'id': project_id, 'type': 'Project'}], ['sg_status_list', 'is_not', 'omt']]
        data = self.sg.find('Asset', _filter, ['id', 'code', 'sg_asset_type'])

        return data
        # sequences, shots, sets,

query = shotgridQuery()

if __name__ == '__main__':
    pass