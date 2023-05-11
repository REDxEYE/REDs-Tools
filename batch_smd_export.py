#############################################
# by: Davi (Debiddo) Gooz, free to use
#############################################

import bpy, os, addon_utils


class VALVE_OT_BatchExportActions(bpy.types.Operator):
    """batch exports all Actions into its own file.
    use with Blender Source Tools"""
    bl_idname = "valve.batch_export_actions"
    bl_label = "Batch Action Export"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        # disable the operator if no Armature object is selected
        return context.active_object and context.active_object.type == 'ARMATURE'

    def execute(self, context):
        bst, _ = addon_utils.check("io_scene_valvesource")
        if not bst:
            self.report({"ERROR"}, "Blender Source Tools is not found!\nHow did you get this error!?")
            return {'FINISHED'}
        context.active_object.type == 'OBJECT'
        for a in bpy.data.actions:
            context.object.animation_data.action = bpy.data.actions.get(a.name)
            bpy.ops.export_scene.smd()

        return {'FINISHED'}

class VALVE_OT_BatchExportActionsRetarget(bpy.types.Operator):
    """This will export all Actions, batch set two Armatures use same Action and export the Action for the Active Armature.
    use with Blender Source Tools"""
    bl_idname = "valve.batch_export_actions_retarget"
    bl_label = "Batch Action Export Retarget"
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
        bst, _ = addon_utils.check("io_scene_valvesource")
        if not bst:
            self.report({"ERROR"}, "Blender Source Tools is not found!\nHow did you get this error!?")
            return {'FINISHED'}
        context.active_object.type == 'OBJECT'
        # This will use just selected Objects 0 and 1
        arm1 = bpy.context.object
        arm2 = [ob for ob in bpy.data.objects if ob.select_get()]
        arm2.remove(arm1)
        arm2 = arm2[0]

        # Set Armature to export as Active
        bpy.context.view_layer.objects.active = arm1

        # just incase blender doesn't deselect for any reason
        arm2.select = False

        # I need names
        arm1 = arm1.name
        arm2 = arm2.name

        for a in bpy.data.actions:

            # I need to update the object every call, because Blender Source Tools bake duplicate objects so the object changes every export
            armature_export = bpy.context.scene.objects[arm1]
            armature_target = bpy.context.scene.objects[arm2]

            # Set Action and make both objects use the same Action
            armature_target.animation_data.action = armature_export.animation_data.action = a

            # Finnaly expot
            bpy.ops.export_scene.smd()

        return {'FINISHED'}
