import bpy

from bpy.props import *

from .bone_table import bone_table_valvebiped, bone_table_bip


class View3DTools:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"


# noinspection PyPep8Naming
class VIEW3D_PT_ToolsPanel(View3DTools, bpy.types.Panel):
    bl_idname = 'VALVE_PT_TOOLSPANEL'
    bl_label = 'Source Engine tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        row = layout.row()
        row.label(text="Target armature")
        row.prop_search(scn, "Armature", scn, "objects", text='', icon="ARMATURE_DATA")
        row.label(text="Target Head")
        row.prop_search(scn, "HeadObject", scn, "objects", text='', icon="OUTLINER_OB_MESH")


# noinspection PyPep8Naming
class VIEW3D_PT_RenameTools(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.rename_panel'
    bl_label = 'Renaming tools'
    bl_parent_id = 'VALVE_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Rename tools")
        box = layout.box()
        box.operator("valve.renamechainpopup")
        box.separator()
        box.label(text='Choose name format')
        box.prop(scn, 'NameFormat')
        box.separator()
        box.prop(scn, 'BoneChains')
        box.operator('valve.renamechain')


# noinspection PyPep8Naming
class VIEW3D_PT_ArmatureTools(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.armature_panel'
    bl_label = 'Armature tools'
    bl_parent_id = 'VALVE_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Armature tools")
        layout.label(text="Work with active armature")
        box = layout.box()
        box.operator("valve.cleanbones")
        box.operator("valve.cleanbonesconstraints")
        box.operator('valve.compare_armatures')

        row = box.row()
        row.operator("rename.biped")
        row.operator("rename.bip")

        row = box.row()
        row.prop(scn, 'NameTemplate', icon='TEXT')
        row.operator('rename.chain')

        box.operator('armature.connect')
        box.operator('armature.merge')


# noinspection PyPep8Naming
class VIEW3D_PT_TrasnferShapes(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.shape_transfer'
    bl_label = 'Transfer shapes'
    bl_parent_id = 'VALVE_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.operator('red_utils.transfer_shapes')
        layout.operator('red_utils.bake_shape_ranges')
        layout.operator('red_utils.bake_shape')
        box = layout.box()
        box.prop(scn, 'ForwardAxis')
        box.prop(scn, 'SplitPower')
        box.operator('red_utils.create_stereo_split')
