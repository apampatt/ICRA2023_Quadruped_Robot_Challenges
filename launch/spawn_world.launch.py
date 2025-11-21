#!/usr/bin/env python3

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Declare arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='competition.world',
        description='SDF world file to load'
    )

    # Package paths
    pkg_this = get_package_share_directory('ICRA2023_Quadruped_Competition')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Construct full path to the world
    world_path = PathJoinSubstitution([
        pkg_this, 'worlds', LaunchConfiguration('world')
    ])

    # Ensure Gazebo can find the package's models
    set_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=os.path.join(pkg_this, 'models') + ':' + os.environ.get('GAZEBO_MODEL_PATH', '')
    )

    # Include Gazebo itself
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'world': world_path,
            'verbose': 'true'
        }.items(),
    )

    return LaunchDescription([
        world_arg,
        set_model_path,
        gazebo
    ])
