from collections import OrderedDict
import re
from openpyxl import load_workbook
import os.path
import wget

DEFAULT_FILENAME='FedRAMP-Moderate-HHH-Baseline-Controls-2016-05-18.xlsx'
DEFAULT_INPUT_XLSX='https://s3.amazonaws.com/sitesusa/wp-content/uploads/sites/482/2016/07/{}'.format(DEFAULT_FILENAME)

class Control(object):
    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.family = name[0:2]
        self.text = text
        self.narrative_keys = []

def _find_or_get_file(filename, url):
    path = './{}'.format(filename)
    if os.path.isfile(path):
        print('Found existing file: {}'.format(path))
    else:
        print('Could not find file: {}'.format(path))
        print('Downloading...')

        #response = requests.get(url, stream=True)
        import pdb; pdb.set_trace()
        wget.download(url, out=filename)
        #with open('./{}'.format(filename), 'wb') as f:
        #    f.write(response.content)

def _get_controls():

    controls = OrderedDict()

    workbook = load_workbook(DEFAULT_FILENAME)
    if workbook.active._cells[(3, 2)].value != 'AC-01':
        raise Exception("Unrecognized format, expected cell B3 to have value 'AC-01'")
    for row in workbook.active.iter_rows(min_row=3):
        control = row[3].value
        title = row[4].value
        text = row[5].value
        if None in [control, title, text]:
            continue
        new_control = Control(control, title, text)

        # 0 Count
        # 1 SORT ID
        # 2 Family
        # 3 ID
        # 4 Control Name
        # 5 "NIST Control Description (From NIST SP 800-53r4 1/23/15)"
        # 6 "Moderate 325"
        # 7 "Moderate FedRAMP-Defined Assignment / Selection Parameters (Numbering matches SSP)"
        # 8 LM Additional FedRAMP Requirements and Guidance
        # 9 Parameter,

        isKeys = 0
        for line in text.splitlines():
            matchObj = re.match(r'\s{0,2}([a-z])\.\s.+', line)
            matchObj2 = re.match(r'\s{0,2}\(([a-z])\)\s.+', line)
            if matchObj:
                isKeys = isKeys + 1
                new_control.narrative_keys.append(matchObj.group(1))
            elif matchObj2:
                isKeys = isKeys + 1
                new_control.narrative_keys.append(matchObj2.group(1))
        if isKeys < 1:
            new_control.narrative_keys.append(control)
        if isKeys == 1:
            raise Exception("weird, only one match for {}".format(control))
        controls[control] = new_control
    return controls

def parse(filename=DEFAULT_FILENAME, url=DEFAULT_INPUT_XLSX):
    _find_or_get_file(filename, url)
    return _get_controls()
