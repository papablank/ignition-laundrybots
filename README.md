# Automated Laundry

This repository contains the concept and simulation for an automated assembly line where a cell of robots wash, dry, fold and inspect clothing. The robots are controlled by an Allen Bradley PLC, while human operators interact with the system through HMI screens developed using Ignition by Inductive Automation. Custom Python scripts are used to extend and integrate functions between the PLC and HMI.

## Features

- **PLC Control**: Uses an Allen Bradley PLC to drive robot motions and process sequences.
- **HMI Integration**: HMI screens built in Ignition provide a user-friendly interface for monitoring and control.
- **Python Extensions**: Custom Python scripts extend PLC functionality on the HMI side.
- **Simulation**: Documentation and scripts to help set up a simulation environment for testing.

## Repository Structure

- **docs/**: Detailed documentation including system overview, architecture diagrams, and requirements.
- **plc_program/**: Contains sample ladder logic diagrams and structured text code snippets.
- **hmi/**: Ignition project files and Python extension scripts.
- **simulation/**: Guidelines and assets for simulating the cell.
- **scripts/**: Python scripts to interface with the PLC for testing or data logging.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/papablank/ignition-laundrybots.git
   cd ignition-laundrybots
