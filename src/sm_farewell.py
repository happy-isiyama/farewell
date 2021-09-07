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

#sys.path.insert(0, '/home/athome/catkin_ws/src/mimi_common_pkg/scripts')
#from common_action_client import *
#from common_function import *

class StartFarewell(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
        rospy.loginfo('StartFarewell')
        return 'outcome1'
        return'outcome2'

class StartRecog(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('StrtRecog')
        return 'outcome3'

class ActRecoginition(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome4'])

    def execute(self,userdata):
        rospy.loginfo('ActRecoginition')
        return 'outcome4'

class DeliverCoat(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['outcome6'])

    def execute(self, userdata):
        rospy.loginfo('DeliverCoat')
        return 'outcome6'

class SendOff(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                outcomes=['outcome7', 'outcome8'])

    def execute(self, userdata):
        rospy.loginfo('SendOff')
        return 'outcome7'
        #return'outcomee8'

def main():
   # speak('start farewell')

#---------------------------------------------------
    #Create the top level SMACH state machine
    sm_top = smach.StateMachine(outcomes=['FINISH'])

    #Open the container
    with sm_top:

        smach.StateMachine.add('FARST_PHASE',StartFarewell(),
                transitions={
                    'outcome1':'SUB1',  
                    'outcome2':'FINISH'}) 

        #----------------------------------------------        
        #Create the sub1 SMACH state machine
        sm_sub1 = smach.StateMachine(outcomes=['outcome5'])
        
        #Open the container
        with sm_sub1:

            smach.StateMachine.add('SET', StartRecog(),
                transitions={
                    'outcome3':'RECOG'})

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
                    'outcome8':'FARST_PHASE'})

        outcomes = sm_top.execute()

if __name__== '__main__':
    rospy.init_node('sm_basic_function')
    main()






