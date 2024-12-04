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
        armatures = [ob for ob in context.selected_objects if ob.type == 'ARMATURE']
        if len(armatures) < 2:
            cls.poll_message_set("You need select two Armatures")
            return False
        if not context.active_object.type == 'ARMATURE':
            cls.poll_message_set("Active Object must be Armature")
            return False
        return True

    def execute(self, context):
        ref_ob = context.object
        other_ob = [ob for ob in bpy.data.objects if ob.select_get() and ob.type == 'ARMATURE']
        other_ob.remove(ref_ob)
        #ob = other_ob[0] # target only one armature

        for ob in other_ob:
            context.view_layer.objects.active = ob

            bpy.ops.object.mode_set(mode='POSE')
            for bone in ref_ob.pose.bones:
                if bone.name in ob.pose.bones:
                    bpy.ops.object.mode_set(mode='POSE')
                    ob.pose.bones[bone.name].matrix = bone.matrix
                    bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}
