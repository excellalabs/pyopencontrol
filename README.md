# pyopencontrol

A library to generate opencontrol compliant yaml

# What does this do?

This library outputs text that looks like this:

```yaml
- control_key: AC-1 # ACCESS CONTROL POLICY AND PROCEDURES
  standard_key: NIST-800-53
  narrative:
  - key: a
    text: >
      TBD
  - key: b
    text: >
      TBD

- control_key: AC-2 # ACCOUNT MANAGEMENT
  standard_key: NIST-800-53
  narrative:
  - key: a
    text: >
      TBD
  - key: b
    text: >
      TBD
  - key: c
    text: >
      TBD
  ...
```

# How to

First, you'll need to download a properly formatted XLSX document provided by FedRAMP to populate all the control_keys. For example:

https://s3.amazonaws.com/sitesusa/wp-content/uploads/sites/482/2016/07/FedRAMP-Moderate-HHH-Baseline-Controls-2016-05-18.xlsx

Next, you'll need to run a script similar to the following in the same directory as the XLSX file:

```python
from pyopencontrol import parse, print_yaml

parse()
print_yaml()
```
