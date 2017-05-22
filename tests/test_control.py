from pyopencontrol.control import Control
import pytest

class TestControl:

    def test_key_parse_with_only_one_key(self):
        # Arrange
        ctl = Control('1', '1', 'test', 'test')
        # override the text so we can test the _parse_narrative_keys function
        ctl.text = '''The organization:
 a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]:
   1. A risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance'''
        
        # Act
        # Assert
        with pytest.raises(Exception):
            ctl._parse_narrative_keys()

    def test_key_parse_with_period_based_keys(self):
        # Arrange
        ctl = Control('1', '1', 'test', 'test')
        # override the text so we can test the _parse_narrative_keys function
        ctl.text = '''The organization:
 a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]:
   1. A risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
   2. Procedures to facilitate the implementation of the risk assessment policy and associated risk assessment controls; and
 b. Reviews and updates the current:
   1. Risk assessment policy [Assignment: organization-defined frequency]; and
   2. Risk assessment procedures [Assignment: organization-defined frequency].'''

        # Act
        ctl._parse_narrative_keys()

        # Assert
        assert ctl.narrative_keys == ['a', 'b']

    def test_key_parse_with_parenthese_based_keys(self):
        # Arrange
        ctl = Control('1', '1', 'test', 'test')
        # override the text so we can test the _parse_narrative_keys function
        ctl.text = '''The organization:
 (a)   Implements procedures for the use of maintenance personnel that lack appropriate security clearances or are not U.S. citizens, that include the following requirements:
   (1)   Maintenance personnel who do not have needed access authorizations, clearances, or formal access approvals are escorted and supervised during the performance of maintenance and diagnostic activities on the information system by approved organizational personnel who are fully cleared, have appropriate access authorizations, and are technically qualified;
  (2)   Prior to initiating maintenance or diagnostic activities by personnel who do not have needed access authorizations, clearances or formal access approvals, all volatile information storage components within the information system are sanitized and all nonvolatile storage media are removed or physically disconnected from the system and secured; and
 (b)   Develops and implements alternate security safeguards in the event an information system component cannot be sanitized, removed, or disconnected from the system.'''

        # Act
        ctl._parse_narrative_keys()

        # Assert
        assert ctl.narrative_keys == ['a', 'b']

    def test_key_parse_with_period_based_keys_and_sameline_key_at_end(self):
        # Arrange
        ctl = Control('1', '1', 'test', 'test')
        # override the text so we can test the _parse_narrative_keys function
        ctl.text = '''The organization:
 a. Obtains administrator documentation for the information system, system component, or information system service that describes:
   1. Secure configuration, installation, and operation of the system, component, or service;
   2. Effective use and maintenance of security functions/mechanisms; and
   3. Known vulnerabilities regarding configuration and use of administrative (i.e., privileged) functions;
 b. Obtains user documentation for the information system, system component, or information system service that describes:
   1. User-accessible security functions/mechanisms and how to effectively use those security functions/mechanisms;
   2. Methods for user interaction, which enables individuals to use the system, component, or service in a more secure manner; and
   3. User responsibilities in maintaining the security of the system, component, or service;
 c. Documents attempts to obtain information system, system component, or information system service documentation when such documentation is either unavailable or nonexistent and [Assignment: organization-defined actions] in response;
 d. Protects documentation as required, in accordance with the risk management strategy; and e. Distributes documentation to [Assignment: organization-defined personnel or roles]. 

Supplemental Guidance:  This control helps organizational personnel understand the implementation and operation of security controls associated with information systems, system components, and information system services. Organizations consider establishing specific measures to determine the quality/completeness of the content provided. The inability to obtain needed documentation may occur, for example, due to the age of the information system/component or lack of support from developers and contractors. In those situations, organizations may need to recreate selected documentation if such documentation is essential to the effective implementation or operation of security controls. The level of protection provided for selected information system, component, or service documentation is commensurate with the security category or classification of the system. For example, documentation associated with a key DoD weapons system or command and control system would typically require a higher level of protection than a routine administrative system. Documentation that addresses information system vulnerabilities may also require an increased level of protection. Secure operation of the information system, includes, for example, initially starting the system and resuming secure system operation after any lapse in system operation. Related controls: CM-6, CM-8, PL-2, PL-4, PS-2, SA-3, SA-4.

References: None.'''

        # Act
        ctl._parse_narrative_keys()

        # Assert
        assert ctl.narrative_keys == ['a', 'b', 'c', 'd', 'e']

    def test_key_parse_with_parenthese_based_keys_and_sameline_key_at_end(self):
        # Arrange
        ctl = Control('1', '1', 'test', 'test')
        # override the text so we can test the _parse_narrative_keys function
        ctl.text = '''The organization:
 (a) Establishes and administers privileged user accounts in accordance with a role-based access scheme that organizes allowed information system access and privileges into roles;
 (b) Monitors privileged role assignments; and
 (c) Takes [Assignment: organization-defined actions] when privileged role assignments are no longer appropriate and (d) made up text for testing purposes

Supplemental Guidance: Privileged roles are organization-defined roles assigned to individuals that allow those individuals to perform certain security-relevant functions that ordinary users are not authorized to perform. These privileged roles include, for example, key management, account management, network and system administration, database administration, and web administration.'''

        # Act
        ctl._parse_narrative_keys()

        # Assert
        assert ctl.narrative_keys == ['a', 'b', 'c', 'd']
