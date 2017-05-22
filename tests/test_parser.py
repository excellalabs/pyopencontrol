from pyopencontrol.control import Control
from pyopencontrol.parser import parse

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

class TestParser:

    def test_find_existing_file(self):
        pass # TODO

    def test_get_file(self):
        pass # TODO

    @patch('pyopencontrol.parser._get_controls')
    @patch('pyopencontrol.parser._find_or_get_file')
    def test_cm3_2_injected_in_right_slot(self, mock_find, mock_get_controls):
        # Arrange
        control1 = Control('AC-03 (01)', 'AC-3 (1)', 'name', 'text')
        control2 = Control('CM-02', 'CM-2', 'name', 'text')
        control3 = Control('CM-03', 'CM-3', 'name', 'text')
        control4 = Control('CM-04', 'CM-4', 'name', 'text')
        controls = [control1, control2, control3, control4]
        mock_get_controls.return_value = controls

        # Act
        results = parse()

        # Assert
        assert list(results.keys()) == ['AC-3 (1)', 'CM-2', 'CM-3', 'CM-3 (2)', 'CM-4']
