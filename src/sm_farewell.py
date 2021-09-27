#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------
#Title:farewell
#Author:Ishiyama Yuki
#Data:2021/8/3~
#Memo:
#----------------------------------------------
#ROS
import sys
import rospy
import smach
import smach_ros

#sys.path.insert(0, '/home/athome/catkin_ws/src/happymimi_apps/')
#from happymimi_teleop import *
#from happymimi_voice.srv import SpeechToText

class StartFarewell(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'],
                                    input_keys=['count_in'])#試行回数のカウント
        #self.stt=rospy.ServiceProxy('/stt_server',SpeechToText)
        #self.pub


    def execute(self, userdata):
        if userdata.count_in == 2:
            return 'outcome2'
        rospy.loginfo('StartFarewell')
        #speak('Please tell me the name of gest')
        #register_object()
        rospy.loginfo('Enter The Room')
        #enterTheRoomAC(0.8)
        #location_list = SetLocationServer('living room')
        #NaviLocationServer(location_list)
        return 'outcome1'

class StartRecog(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=['outcome3'])

    def execute(self, userdata):
        #rospy.loginfo('StrtRecog')
        #rotateAngle(-90)
        #openpose
        return 'outcome3'

class ActRecoginition(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome4'])

    def execute(self,userdata):
        flag = True

        rospy.loginfo('ActRecoginition')
        #while not rospy.is_shutdown() and degree < 180:
            #rorateAngele(60)
            #degeree += 60
            #openpose
        #openpose
        #speak('Mr.fukuda please follow me')
        return 'outcome4'

class DeliverCoat(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['outcome6'])

    def execute(self, userdata):
        rospy.loginfo('DeliverCoat')
        #location_list = SetLocationServer('closet')
        #NavigationServer(location_list)
        return 'outcome6'

class SendOff(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                outcomes=['outcome7', 'outcome8'],
                input_keys=['count_in'],
                output_keys=['count_out'])

    def execute(self, userdata):
        rospy.loginfo('SendOff')
        count = userdata.count_in

        if count > 3:
            return 'outcome7'
        else:
            userdata.count_out = count+1
            return'outcome8'

def main():
    #speak('start farewell')

#---------------------------------------------------
    #Create the top level SMACH state machine
    sm_top = smach.StateMachine(outcomes=['FINISH'])

    #Open the container
    with sm_top:
        sm_top.userdata.sm_count = 0
        smach.StateMachine.add('FARST_PHASE',StartFarewell(),
                transitions={
                    'outcome1':'SUB1',  
                    'outcome2':'FINISH'},
                remapping={
                    'count_in':'sm_count',
                    'count_out':'sm_count'}) 

        #----------------------------------------------        
        #Create the sub1 SMACH state machine
        sm_sub1 = smach.StateMachine(outcomes=['outcome5'])
        
        #Open the container
        with sm_sub1:

            smach.StateMachine.add('SET', StartRecog(),
                transitions={
                    'outcome3':'RECOG'},
                remapping={
                    'count_in':'sm_count',
                    'count_out':'sm_count'})

            smach.StateMachine.add('RECOG', ActRecoginition(),
                transitions={
                    'outcome4':'outcome5'})

        smach.StateMachine.add('SUB1', sm_sub1,
                transitions={
                    'outcome5':'COAT'})

        #---------------------------------------------

        smach.StateMachine.add('COAT', DeliverCoat(),
                transitions={
                    'outcome6':'SENDOFF'})

        smach.StateMachine.add('SENDOFF', SendOff(),
                transitions={
                    'outcome7':'FINISH',
                    'outcome8':'FARST_PHASE'},
                remapping={
                    'count_in':'sm_count',
                    'count_out':'sm_count'})

        outcomes = sm_top.execute()

if __name__== '__main__':
    rospy.init_node('sm_farewell')
    main()






