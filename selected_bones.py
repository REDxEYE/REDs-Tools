##############################################################
# Purpose:
#   Operações que enviam seu resultado para o Clipboard
#
#  por: Davi (Debiddo) Gooz
##############################################################
import bpy

class ARMATURE_OT_WeightBonesClipboard(bpy.types.Operator):
    """Send all weighted bone names to clipboard
    You may use this to make a $bonemerge or $jigglebone list"""
    bl_idname = "valve.weighted_bones_to_clipboard"
    bl_label = "Weighted bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        nm = ""
        for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
            # print(armature.data.bones)
            for bone in armature.data.bones:
                # print(bone.name)
                nm = bone.name + "\n" + nm

        bpy.context.window_manager.clipboard = nm

        return {'FINISHED'}

class ARMATURE_OT_SelectedBonesClipboard(bpy.types.Operator):
    """Copy all selected bones names to clipboard
    You may use this to make a $bonemerge or $jigglebone list"""
    bl_idname = "valve.selected_bones_to_clipboard"
    bl_label = "Selected bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        nm = ""
        for list_of_bones in bpy.context.selected_pose_bones_from_active_object:
            # print(list_of_bones.bone.name)
            nm = list_of_bones.bone.name + "\n" + nm

        bpy.context.window_manager.clipboard = nm

        return {'FINISHED'}

class ARMATURE_OT_SelectedBonesBonemergeClipboard(bpy.types.Operator):
    """Send to clipboard all selected bones formated for $bonemerge"""
    bl_idname = "valve.bonemerge_to_clipboard"
    bl_label = "$bonemerge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        nm = ""
        for list_of_bones in bpy.context.selected_pose_bones_from_active_object:
            # print(list_of_bones.bone.name)
            nm = "$bonemerge \"" + list_of_bones.bone.name + "\"\n" + nm

        bpy.context.window_manager.clipboard = nm

        return {'FINISHED'}
