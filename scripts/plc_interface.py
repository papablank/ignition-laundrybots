
---

## Example Python Script for PLC Communication

You can use a Python library like `pylogix` to communicate with an Allen Bradley PLC for testing or extended functionality. Save this as `scripts/plc_interface.py`:

```python
#!/usr/bin/env python3
"""
A simple Python script to read and write tags on an Allen Bradley PLC using pylogix.
"""

from pylogix import PLC

PLC_IP = "192.168.1.100"  # Replace with your PLC's IP address

def read_plc_tag(tag_name):
    with PLC() as comm:
        comm.IPAddress = PLC_IP
        ret = comm.Read(tag_name)
        if ret.Status == "Success":
            print(f"Tag {tag_name} value: {ret.Value}")
        else:
            print(f"Error reading tag {tag_name}: {ret.Status}")

def write_plc_tag(tag_name, value):
    with PLC() as comm:
        comm.IPAddress = PLC_IP
        ret = comm.Write(tag_name, value)
        if ret.Status == "Success":
            print(f"Successfully wrote {value} to tag {tag_name}")
        else:
            print(f"Error writing tag {tag_name}: {ret.Status}")

if __name__ == '__main__':
    # Example usage:
    read_plc_tag("Robot_Start")
    write_plc_tag("Robot_Start", True)
