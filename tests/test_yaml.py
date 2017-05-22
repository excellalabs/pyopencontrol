from collections import OrderedDict
from pyopencontrol.control import Control
from pyopencontrol import yaml

try:
    from mock import patch, ANY, call
except ImportError:
    from unittest.mock import patch, ANY, call

class TestPrintYaml:
    def test_yaml_control_without_keys_prints_text(self):
        # Arrange
        control = Control('sortid', 'id', 'name', 'text without keys')

        # Act
        result = yaml._generate_yaml_control(control, 'default_text')

        # Assert
        assert '- text' in result
        assert '- key' not in result

    def test_yaml_control_with_keys_prints_key_and_text(self):
        # Arrange
        control = Control('sortid', 'id', 'name', 'text with keys')
        control.narrative_keys = ['keya', 'keyb']

        # Act
        result = yaml._generate_yaml_control(control, 'default_text')

        # Assert
        assert '- text' not in result
        assert '- key: keya' in result
        assert '- key: keyb' in result

    @patch('pyopencontrol.yaml.parse')
    @patch('pyopencontrol.yaml._generate_yaml_control')
    def test_yaml_family_filter_filters_other_families(self, mock_generate_yaml,
                                                       mock_parse):
        # Arrange
        control1 = Control('AC-02', 'AC-2', 'name', 'text with keys')
        control2 = Control('AC-03', 'AC-3', 'name', 'text with keys')
        control3 = Control('AT-02', 'AT-2', 'name', 'text with keys')
        controls = OrderedDict({control1.id: control1,
                                control2.id: control2,
                                control3.id: control3})
        mock_parse.return_value = controls
        calls = [call(control1, ANY, ANY), call(control2, ANY, ANY)]

        # Act
        result = yaml.print_yaml(family='AC')

        # Assert
        assert mock_generate_yaml.call_count == 2
        mock_generate_yaml.assert_has_calls(calls, any_order=True)

    @patch('pyopencontrol.yaml.parse')
    def text_yaml_family_filter_with_no_results(self, mock_parse):
        # Arrange
        control1 = Control('AC-02', 'AC-2', 'name', 'text with keys')
        control2 = Control('AC-03', 'AC-3', 'name', 'text with keys')
        control3 = Control('AT-02', 'AT-2', 'name', 'text with keys')
        controls = OrderedDict({control1.id: control1,
                                control2.id: control2,
                                control3.id: control3})
        mock_parse.return_value = controls

        # Act
        result = yaml.print_yaml(family='AU')

        # Assert
        assert result.is_empty()
