import json
import os

class GameSettings:
    """Shared game settings with JSON persistence"""

    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self._framerate = 60
        self._load_from_json()

    def _load_from_json(self):
        """Load settings from JSON file if it exists"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    data = json.load(f)
                    self.parse_json(data)
                    # Save the JSON data in case we have added any new settings in the code
                    self._save_to_json()
            except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
                print(f"Error loading settings: {e}. Using defaults.")
                self._create_default_settings_file()
        else:
            self._create_default_settings_file()
    
    def _save_to_json(self):
        """Save current settings to JSON file"""
        data = self.build_json_dict()
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def _create_default_settings_file(self):
        """Create default settings file"""
        self._save_to_json()

    def parse_json(self, json_data):
        """Parse the loaded json into the class's properties"""
        self._framerate = json_data.get('framerate', 60)

    def build_json_dict(self):
        """Construct a dictionary from the class's properties that need to be persisted"""
        return {
            'framerate': self._framerate
        }
    
    # Getters and setters for base class properties
    @property
    def framerate(self):
        return self._framerate
    
    @framerate.setter
    def framerate(self, framerate):
        self._framerate = framerate
