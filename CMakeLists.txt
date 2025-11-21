cmake_minimum_required(VERSION 3.5)
project(ICRA2023_Quadruped_Competition)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED)
find_package(gazebo_ros2_control REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(sensor_msgs REQUIRED)


set(dependencies
#  INCLUDE_DIRS include
#  LIBRARIES ICRA2023_Quadruped_Competition
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
  rclcpp
  urdf
  gazebo_ros2_control
  gazebo_ros
  sensor_msgs
)

include_directories(include) 

link_directories(
  ${GAZEBO_LIBRARY_DIRS}
)

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)


# install(DIRECTORY include/ DESTINATION include/${PROJECT_NAME})
install(DIRECTORY worlds DESTINATION share/${PROJECT_NAME})
install(DIRECTORY urdf DESTINATION share/${PROJECT_NAME})
install(DIRECTORY meshes/part DESTINATION share/${PROJECT_NAME})
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY rviz DESTINATION share/${PROJECT_NAME})


ament_export_include_directories(include)
ament_export_dependencies(${dependencies})

ament_package()
