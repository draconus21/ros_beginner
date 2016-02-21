# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "neeth_tbot: 0 messages, 1 services")

set(MSG_I_FLAGS "-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(neeth_tbot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv" NAME_WE)
add_custom_target(_neeth_tbot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "neeth_tbot" "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv" "geometry_msgs/Vector3:geometry_msgs/Twist"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(neeth_tbot
  "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/neeth_tbot
)

### Generating Module File
_generate_module_cpp(neeth_tbot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/neeth_tbot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(neeth_tbot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(neeth_tbot_generate_messages neeth_tbot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv" NAME_WE)
add_dependencies(neeth_tbot_generate_messages_cpp _neeth_tbot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(neeth_tbot_gencpp)
add_dependencies(neeth_tbot_gencpp neeth_tbot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS neeth_tbot_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(neeth_tbot
  "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/neeth_tbot
)

### Generating Module File
_generate_module_lisp(neeth_tbot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/neeth_tbot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(neeth_tbot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(neeth_tbot_generate_messages neeth_tbot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv" NAME_WE)
add_dependencies(neeth_tbot_generate_messages_lisp _neeth_tbot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(neeth_tbot_genlisp)
add_dependencies(neeth_tbot_genlisp neeth_tbot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS neeth_tbot_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(neeth_tbot
  "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/neeth_tbot
)

### Generating Module File
_generate_module_py(neeth_tbot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/neeth_tbot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(neeth_tbot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(neeth_tbot_generate_messages neeth_tbot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/neeth/catkin_ws/src/neeth_tbot/srv/Command.srv" NAME_WE)
add_dependencies(neeth_tbot_generate_messages_py _neeth_tbot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(neeth_tbot_genpy)
add_dependencies(neeth_tbot_genpy neeth_tbot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS neeth_tbot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/neeth_tbot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/neeth_tbot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(neeth_tbot_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(neeth_tbot_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(neeth_tbot_generate_messages_cpp std_srvs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/neeth_tbot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/neeth_tbot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(neeth_tbot_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(neeth_tbot_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(neeth_tbot_generate_messages_lisp std_srvs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/neeth_tbot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/neeth_tbot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/neeth_tbot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(neeth_tbot_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(neeth_tbot_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(neeth_tbot_generate_messages_py std_srvs_generate_messages_py)
