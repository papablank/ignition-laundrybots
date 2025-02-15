# Project Overview: Automated Clothing Wash & Dry Cell

This project aims to design and simulate an automated assembly line for washing and drying clothing. The system consists of:

- **Robots:** Automated units that perform the washing and drying tasks.
- **Allen Bradley PLC:** Controls the operation of the robots and coordinates the process.
- **HMI Screens:** Developed using Ignition by Inductive Automation, these screens allow human operators to monitor and control the process.
- **Python Extensions:** Custom scripts extend the functionality of the PLC and integrate with the HMI for enhanced control and data processing.

## System Components

### 1. Robots
- **Function:** Execute washing and drying operations.
- **Control:** Operated via instructions from the PLC.

### 2. Allen Bradley PLC
- **Role:** Central controller for the automation process.
- **Programming:** Implemented using ladder logic or structured text.
- **Integration:** Communicates with the HMI and Python scripts for real-time operation and monitoring.

### 3. HMI Screens (Ignition)
- **Interface:** Provides a user-friendly graphical interface for operators.
- **Customization:** Extended using Python to implement additional control logic and features.

### 4. Python Extensions
- **Purpose:** Enhance the functionality of the PLC and HMI.
- **Examples:** Scripts to log data, trigger events, or facilitate communication between system components.

## How It Works

1. **Initiation:** The process is started from the HMI, which sends a command to the PLC.
2. **Robot Operation:** The PLC triggers the robots to begin the wash cycle.
3. **Process Monitoring:** Operators monitor the process through the HMI screens, which display real-time data.
4. **Completion:** Once the cycle is complete, the PLC coordinates the drying process and notifies the HMI.

## Next Steps

- **Simulation Setup:** Follow the guidelines in the simulation folder to test and refine the process.
- **Detailed Documentation:** Additional documents in this repository provide further insights into the system architecture, PLC programming, and HMI configuration.

---

This overview provides a high-level look at the project's structure and functionality. As you develop the system, you can expand these sections with more detailed technical information and operational procedures.
