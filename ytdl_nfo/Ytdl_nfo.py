import os
import json
from pathlib import Path
from .nfo import get_config

class Ytdl_nfo:
    def __init__(self, file_path, extractor=None):
        self.path = file_path
        self.dir = os.path.dirname(file_path)

        # Read json data
        with open(self.path, 'r') as f:
            self.data = json.load(f)

        self.extractor = extractor
        if extractor is None:
            self.extractor = self.data['extractor'].lower()

        try:
            self.filename = os.path.splitext(self.data['_filename'])[0]
        except KeyError:
            self.filename = Path(self.path)
        self.nfo = get_config(self.extractor)

    def process(self):
        self.nfo.generate(self.data)
        #self.nfo.print_nfo()
        if self.filename.name[-len('.info.json'):] == '.info.json':
            self.nfo.write_nfo(os.path.join(self.dir, Path(self.filename.parent).joinpath(self.filename.name.replace('.info.json', '.nfo'))))
        else:
            self.nfo.write_nfo(os.path.join(self.dir, self.filename.with_suffix('.nfo')))

    def print_data(self):
        print(json.dumps(self.data, indent=4, sort_keys=True))


