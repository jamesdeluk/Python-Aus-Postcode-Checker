"""checks postcode against aus regional postcodes"""

# pylint: disable=C0103

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

import json


specific_postcodes_file = 'postcodes.txt'
with open(specific_postcodes_file, 'r') as f:
    specific_postcodes = f.read()[1:-1].split(', ')
    specific_postcodes = [int(x) for x in specific_postcodes]

postcodes_lookup_file = 'au_postcodes.json'
with open(postcodes_lookup_file) as f:
    postcodes_lookup = json.load(f)


class CheckerWidget(BoxLayout):
    pass


class CheckerApp(App):

    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '400')
    Config.write()

    def build(self):
        return CheckerWidget()


    def get_regions(self, postcode):
        """get regions"""
        try:
            postcode = int(postcode)
            region_list = []
            for region in postcodes_lookup:
                if region['postcode'] == postcode:
                    region_list.append(region['place_name'])
            return region_list
        except:
            return


    # regionals = []
    # not_regionals = []


    def check(self, postcode):
        """checking code"""
        postcode_input = postcode
        if not postcode_input:
            s += f'Enter something...'
        s = f'{postcode_input}\n\n'
        regions = self.get_regions(postcode_input)
        if (len(postcode_input) != 4) or (not regions):
            s += f'Invalid postcode'
            return s
        elif int(postcode_input) in specific_postcodes:
            s += f'^_^ Regional\n\n'
            # regionals.append(postcode_input)
        else:
            s += f'T_T Not regional\n\n'
            # not_regionals.append(postcode_input)
        for region in regions[:3]:
            s += f'{region}\n'
        return s


if __name__ == "__main__":
    CheckerApp().run()
