
(cl:in-package :asdf)

(defsystem "turtlebot_a1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "MoveBot" :depends-on ("_package_MoveBot"))
    (:file "_package_MoveBot" :depends-on ("_package"))
  ))