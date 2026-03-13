# AirSim MCP Drone Controller

This module provides a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) Server that allows an LLM to control a drone inside Microsoft AirSim (using the `cosysairsim` library).

## Prerequisites

Ensure you have your AirSim environment running and accessible before starting the MCP server.

## Installation

Install the required Python packages:

```bash
pip install cosysairsim mcp numpy
```

## Running the Server

To start the MCP server, you can run it directly if supported by your MCP client, or add it to your host configuration (e.g., Claude Desktop, LM Studio) as a standard `stdio` MCP server using:

```bash
python mcp_server.py
```

*Logs:* Debug information and outputs not meant for the MCP JSON-RPC transport will be safely logged to `mcp_drone.log` in this same directory.

## Available MCP Tools

The server exposes the following drone control tools to the LLM:

- **`drone_arm`**: Arm the drone propellers.
- **`drone_disarm`**: Disarm the drone propellers.
- **`drone_takeoff`**: Takeoff the drone (must be armed first).
- **`drone_move_to_position(x, y, z, velocity)`**: Move the drone to a specific local space coordinate.
- **`drone_move_on_path(path_points, velocity)`**: Move the drone along a list of path points (provided as a JSON string of `{x, y, z}` coordinates).
- **`drone_go_home`**: Return the drone back to its home position and disarm.
- **`drone_stop`**: Stop the drone, return home, and reset.
- **`drone_orbit(speed, iterations, target_x, target_y)`**: Make the drone orbit around a specific coordinate.
- **`drone_get_state`**: Get the current state, including position, velocity, and landed state.
- **`drone_reset`**: Reset the AirSim simulation environment.
