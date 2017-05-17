from pyopencontrol.parser import parse

def _generate_yaml_control(control, default_text, implementation_status=None):
    lines = []
    lines.append("- control_key: {} # {}".format(control.id, control.name.replace('\n', ' ')))
    if implementation_status:
        lines.append("  implementation_status: {}".format(implementation_status))
    lines.append("  standard_key: NIST-800-53")
    lines.append("  narrative:")
    for key in control.narrative_keys:
        if key == control.id:
            lines.append("  - text: >")
            lines.append("      {}".format(default_text))
        else:
            lines.append("  - key: %s" % key)
            lines.append("    text: >")
            lines.append("      {}".format(default_text))
    return '\n'.join(lines)+'\n'

def print_yaml(family=None, default_text='TBD', implementation_status=None):
    controls = parse()
    for _, control in controls.items():
        if not family or family in control.id:
            print(_generate_yaml_control(control, default_text,
                                         implementation_status))
