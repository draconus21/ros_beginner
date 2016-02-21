# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "turtlebot_a1: 1 messages, 1 services")

set(MSG_I_FLAGS "-Iturtlebot_a1:/home/neeth/catkin_ws/src/turtlebot_a1/msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(turtlebot_a1_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv" NAME_WE)
add_custom_target(_turtlebot_a1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "turtlebot_a1" "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv" "geometry_msgs/Vector3:geometry_msgs/Twist"
)

get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg" NAME_WE)
add_custom_target(_turtlebot_a1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "turtlebot_a1" "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlebot_a1
)

### Generating Services
_generate_srv_cpp(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlebot_a1
)

### Generating Module File
_generate_module_cpp(turtlebot_a1
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlebot_a1
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(turtlebot_a1_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(turtlebot_a1_generate_messages turtlebot_a1_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_cpp _turtlebot_a1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_cpp _turtlebot_a1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlebot_a1_gencpp)
add_dependencies(turtlebot_a1_gencpp turtlebot_a1_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlebot_a1_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlebot_a1
)

### Generating Services
_generate_srv_lisp(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlebot_a1
)

### Generating Module File
_generate_module_lisp(turtlebot_a1
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlebot_a1
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(turtlebot_a1_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(turtlebot_a1_generate_messages turtlebot_a1_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_lisp _turtlebot_a1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_lisp _turtlebot_a1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlebot_a1_genlisp)
add_dependencies(turtlebot_a1_genlisp turtlebot_a1_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlebot_a1_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1
)

### Generating Services
_generate_srv_py(turtlebot_a1
  "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1
)

### Generating Module File
_generate_module_py(turtlebot_a1
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(turtlebot_a1_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(turtlebot_a1_generate_messages turtlebot_a1_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/srv/MoveBot.srv" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_py _turtlebot_a1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/neeth/catkin_ws/src/turtlebot_a1/msg/Vel.msg" NAME_WE)
add_dependencies(turtlebot_a1_generate_messages_py _turtlebot_a1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlebot_a1_genpy)
add_dependencies(turtlebot_a1_genpy turtlebot_a1_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlebot_a1_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlebot_a1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlebot_a1
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(turtlebot_a1_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(turtlebot_a1_generate_messages_cpp sensor_msgs_generate_messages_cpp)
add_dependencies(turtlebot_a1_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlebot_a1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlebot_a1
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(turtlebot_a1_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(turtlebot_a1_generate_messages_lisp sensor_msgs_generate_messages_lisp)
add_dependencies(turtlebot_a1_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlebot_a1
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(turtlebot_a1_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(turtlebot_a1_generate_messages_py sensor_msgs_generate_messages_py)
add_dependencies(turtlebot_a1_generate_messages_py std_msgs_generate_messages_py)
