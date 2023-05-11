##########################################
# Purpose: Copy the entire pose between two different armatures
#
#  por: Davi (Debiddo) Gooz
##########################################

import bpy

class VALVE_OT_CopyPose(bpy.types.Operator):
    """Copy active armature pose and apply to the other selected armature"""
    bl_idname = "valve.copypose"
    bl_label = "Copy active pose"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # Check if both armatures are selected
        if len(context.selected_objects) != 2:
            return False
        armatures = [obj for obj in context.selected_objects if obj.type == 'ARMATURE']
        if len(armatures) != 2:
            return False
        return True

    def execute(self, context):
        ref_ob = bpy.context.object
        other_ob = [ob for ob in bpy.data.objects if ob.select_get()]
        other_ob.remove(ref_ob)
        other_ob = other_ob[0]

        bpy.context.view_layer.objects.active = other_ob

        bpy.ops.object.mode_set(mode='OBJECT')
        for bone in ref_ob.pose.bones:
            if bone.name in other_ob.pose.bones:
                bpy.ops.object.mode_set(mode='POSE')
                other_ob.pose.bones[bone.name].matrix = bone.matrix
                bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}
