##########################################
# Purpose: 
#
#  por: Davi (Debiddo) Gooz
##########################################

import bpy
from mathutils import Matrix

helper_string = '<helper> {Helper} {HelperParent} {ControllerParent} {Controller}'
basepos_string = '<basepos> {HelperBaseLocation}'
trugger_string = '<trigger> 90 {ControllerRotation} {HelperRotation} {HelperLocation}'


class VALVE_OT_ProceduralBone(bpy.types.Operator):
    """Copy active armature pose and apply to the other selected armature"""
    bl_idname = "valve.proceduralbone"
    bl_label = "Copy Proceduralbone"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        if (context.active_object):
            if context.active_object.type == 'ARMATURE':
                if context.active_object.mode == 'POSE':
                    return True
        return False

    def execute(self, context):

        selected_bones = context.selected_pose_bones
        
        if len(selected_bones) != 2:
            print("Please select exactly two bones")
        else:

            Helper = selected_bones[0]
            Controller = selected_bones[1]
            HelperParent = Helper.parent
            ControllerParent = Controller.parent
            HelperBaseLocation = Helper.head_local
            ControllerRotation = 0
            HelperRotation = 0
            HelperLocation = 0

            #return Helper, Controller, HelperParent, ControllerParent, HelperBaseLocation, ControllerRotation, HelperRotation, HelperLocation

        context.sourceops.pose_bone_transforms(type='TRANSLATION')
        context.sourceops.pose_bone_transforms(type='ROTATION')

        return {'FINISHED'}

    def get_relative_transforms(bone1_name, bone2_name):
        armature = bpy.context.active_object
        bone1 = armature.pose.bones.get(bone1_name)
        bone2 = armature.pose.bones.get(bone2_name)

        if bone1 and bone2:
            bone1_matrix = bone1.parent.matrix.inverted() @ bone1.matrix
            bone2_matrix = bone2.parent.matrix.inverted() @ bone2.matrix

            bone1_loc, bone1_rot, bone1_scale = bone1_matrix.decompose()
            bone2_loc, bone2_rot, bone2_scale = bone2_matrix.decompose()

            return bone1_loc, bone1_rot, bone2_loc, bone2_rot
        else:
            print("One or both bones not found")
