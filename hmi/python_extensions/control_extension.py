# This script can be attached to a button in the Ignition Designer to trigger PLC functions.

def trigger_robot_cycle():
    """
    Trigger a full wash and dry cycle by writing to the PLC tag.
    """
    plc_tag = "Robot_Cycle_Start"
    new_value = True  # or use a value to represent a command code

    try:
        system.tag.writeBlocking([plc_tag], [new_value])
        system.gui.messageBox("Robot cycle triggered successfully!")
    except Exception as e:
        system.gui.errorBox("Failed to trigger robot cycle: " + str(e))

# Bind the function to a button's onClick event in the Ignition Designer.
