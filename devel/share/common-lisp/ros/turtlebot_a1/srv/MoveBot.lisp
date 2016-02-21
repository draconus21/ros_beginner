; Auto-generated. Do not edit!


(cl:in-package turtlebot_a1-srv)


;//! \htmlinclude MoveBot-request.msg.html

(cl:defclass <MoveBot-request> (roslisp-msg-protocol:ros-message)
  ((vel
    :reader vel
    :initarg :vel
    :type geometry_msgs-msg:Twist
    :initform (cl:make-instance 'geometry_msgs-msg:Twist)))
)

(cl:defclass MoveBot-request (<MoveBot-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveBot-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveBot-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlebot_a1-srv:<MoveBot-request> is deprecated: use turtlebot_a1-srv:MoveBot-request instead.")))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <MoveBot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlebot_a1-srv:vel-val is deprecated.  Use turtlebot_a1-srv:vel instead.")
  (vel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveBot-request>) ostream)
  "Serializes a message object of type '<MoveBot-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveBot-request>) istream)
  "Deserializes a message object of type '<MoveBot-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveBot-request>)))
  "Returns string type for a service object of type '<MoveBot-request>"
  "turtlebot_a1/MoveBotRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveBot-request)))
  "Returns string type for a service object of type 'MoveBot-request"
  "turtlebot_a1/MoveBotRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveBot-request>)))
  "Returns md5sum for a message object of type '<MoveBot-request>"
  "15f94ffed970f2e1c99ad7dc815c974d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveBot-request)))
  "Returns md5sum for a message object of type 'MoveBot-request"
  "15f94ffed970f2e1c99ad7dc815c974d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveBot-request>)))
  "Returns full string definition for message of type '<MoveBot-request>"
  (cl:format cl:nil "geometry_msgs/Twist vel~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveBot-request)))
  "Returns full string definition for message of type 'MoveBot-request"
  (cl:format cl:nil "geometry_msgs/Twist vel~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveBot-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveBot-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveBot-request
    (cl:cons ':vel (vel msg))
))
;//! \htmlinclude MoveBot-response.msg.html

(cl:defclass <MoveBot-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:integer
    :initform 0))
)

(cl:defclass MoveBot-response (<MoveBot-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveBot-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveBot-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlebot_a1-srv:<MoveBot-response> is deprecated: use turtlebot_a1-srv:MoveBot-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <MoveBot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlebot_a1-srv:status-val is deprecated.  Use turtlebot_a1-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveBot-response>) ostream)
  "Serializes a message object of type '<MoveBot-response>"
  (cl:let* ((signed (cl:slot-value msg 'status)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveBot-response>) istream)
  "Deserializes a message object of type '<MoveBot-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveBot-response>)))
  "Returns string type for a service object of type '<MoveBot-response>"
  "turtlebot_a1/MoveBotResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveBot-response)))
  "Returns string type for a service object of type 'MoveBot-response"
  "turtlebot_a1/MoveBotResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveBot-response>)))
  "Returns md5sum for a message object of type '<MoveBot-response>"
  "15f94ffed970f2e1c99ad7dc815c974d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveBot-response)))
  "Returns md5sum for a message object of type 'MoveBot-response"
  "15f94ffed970f2e1c99ad7dc815c974d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveBot-response>)))
  "Returns full string definition for message of type '<MoveBot-response>"
  (cl:format cl:nil "int64 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveBot-response)))
  "Returns full string definition for message of type 'MoveBot-response"
  (cl:format cl:nil "int64 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveBot-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveBot-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveBot-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveBot)))
  'MoveBot-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveBot)))
  'MoveBot-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveBot)))
  "Returns string type for a service object of type '<MoveBot>"
  "turtlebot_a1/MoveBot")