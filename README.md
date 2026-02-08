 # Autonomous Navigation of a Mobile Robot
### Bachelor’s Thesis Project


**Focus:** ROS-based outdoor autonomous navigation using SLAM, localization, and path planning in simulation

---

## Overview

This repository contains the implementation and configuration files developed as part of my Bachelor’s Thesis on **Autonomous Mobile Robot Navigation**. The project demonstrates a complete autonomous navigation pipeline using **ROS (Robot Operating System)**.

The system is designed around a differential-drive mobile robot (Pioneer P3-DX–style platform) and validated in a simulated environment. Key features include:

* **Robot Simulation:** Full environment simulation in Gazebo.
* **Mapping:** 2D occupancy grid generation using SLAM (gmapping).
* **Localization & Navigation:** Robust pose estimation using the ROS Navigation Stack.
* **Path Planning:** Global and local planning with dynamic costmaps.
* **Visualization:** Real-time state and sensor visualization using RViz.

## Objectives

* Design and implement an autonomous navigation framework using ROS.
* Enable a mobile robot to navigate from a start point to a goal while avoiding obstacles.
* Integrate SLAM, localization, and motion planning algorithms.
* Tune navigation parameters for stable and reliable motion.
* Provide a reproducible, simulation-based setup suitable for academic evaluation.

## System Architecture

The autonomous navigation pipeline consists of the following modular components:

1.  **Simulation (Gazebo):** Simulates the physical robot dynamics, sensors (Lidar/Odometry), and the environment.
2.  **Mapping (SLAM – gmapping):** Generates a 2D occupancy grid map using laser scan data.
3.  **Localization:** Uses the generated map and sensor data to estimate the robot's pose in real-time.
4.  **Path Planning (move_base):**
    * **Global Planner:** Computes the optimal path to the destination based on the static map.
    * **Local Planner:** Handles obstacle avoidance and generates velocity commands ($v, \omega$) for the robot base.
5.  **Visualization (RViz):** Displays the robot model, live costmaps, laser scans, and navigation goals.

## Key Components Explained

###  Master.py
Acts as the main controller or coordination node. It interfaces with ROS topics and services and is responsible for triggering navigation behavior and handling goal execution logic.

###  Run.launch
The primary entry point for the project. It launches the full navigation stack, including:
* Gazebo Simulation
* SLAM nodes
* `move_base`
* RViz visualization tools
* Parameter loading from `simulation_params/`
