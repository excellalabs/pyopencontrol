import re

class Control(object):
    def __init__(self, sortid, id, name, text):
        self.sortid = sortid
        self.id = id
        self.name = name
        self.family = name[0:2]
        self.text = text
        self.narrative_keys = []
        self._parse_narrative_keys()

    def _parse_narrative_keys(self):
        default_key_regex_list = [
            r'\s{0,2}([a-z])\.\s.+',
            r'\s{0,2}\(([a-z])\)\s.+',
        ]
        self._key_search(default_key_regex_list)

        # Some controls embed the last key without a newline.
        # For example, SA-5
        # let's see if another key exists.
        # TODO reduce duplicate code
        if self.narrative_keys:
            key_after_last = chr(ord(self.narrative_keys[-1]) + 1)
            extra_key_regex_list = [
                r'.+\sand\s([{}])\.\s.+'.format(key_after_last),
                r'.+\sand\s\(([{}])\)\s.+'.format(key_after_last),
            ]
            self._key_search(extra_key_regex_list)

        if len(self.narrative_keys) == 1:
            raise Exception("weird, only one key match for {}".format(self.id))


    def _key_search(self, regex_list):
        for line in self.text.splitlines():
            for regex_match in regex_list:
                matchObj = re.match(regex_match, line)
                if matchObj:
                    self.narrative_keys.append(matchObj.group(1))
