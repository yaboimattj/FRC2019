#!/usr/bin/env python3

import wpilib, magicbot



class FROGbot(magicbot.MagicRobot):
    def createObjects(self):
        """ Method to set up all components """
        # Create DriveTrain
        
        # Set up Joystick
        pass

    def teleopInit(self):
        """Optional method to initialize anything for teleop control"""
        pass

    def teleopPeriodic(self):
        """Called on each iteration of the control loop"""
        pass


if __name__ == "__main__":
    wpilib.run(FROGbot)