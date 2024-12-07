import bpy

from bpy.props import *
import addon_utils
#from .bone_table import bone_table_valvebiped, bone_table_bip


class View3DTools:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"


class VIEW3D_PT_TOOLSPANEL(View3DTools, bpy.types.Panel):
    """Master Control for all bellow tools"""
    bl_idname = 'VIEW3D_PT_TOOLSPANEL'
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


class VIEW3D_PT_ArmatureTools(View3DTools, bpy.types.Panel):
    """All related options related to aid ARMATURE"""
    #bl_idname = 'valve.armature_panel'
    bl_label = 'Armature tools'
    bl_parent_id = 'VIEW3D_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = False
        layout.use_property_decorate = False

        layout.label(text="Work with active armature")

        split = layout.split()
        #box = layout.box()
        col = split.column()
        row = col.row(align=True)

        # column = box.column(align=True)
        # column.separator()

        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Bone Operators:")
        row = col.row(align=True)
        row.operator('valve.bone_viewmode')
        row.operator('valve.bones_shape_clear')
        row.operator('valve.setup_bones_layers')
        #row.operator('valve.comparearmatures')
        col.operator('valve.armature_connect')
        col.operator('valve.armature_merge')
        col.operator('valve.copypose')
        row = col.row(align=True)
        row.operator('armature.bone_location_lock')
        row.operator("pose.constraints_clear")
        row = col.row(align=True)
        col.operator('armature.empty_to_bones', icon='EMPTY_AXIS')

        row = col.row(align=True)
        row.label(text="To Clipboard:")
        row = col.row(align=True)
        row.operator('valve.weighted_bones_to_clipboard')
        row.operator('valve.selected_bones_to_clipboard')
        row.operator('valve.bonemerge_to_clipboard')
        
        # in case SourceOps is present enable this
        '''row.label(text="Procedurals:")
        row = col.row(align=True)
        SourceOps, _ = addon_utils.check("SourceOps")
        if SourceOps:
            row.operator('sourceops.pose_bone_transforms(type="TRANSLATION")', text="Relative Location")
            row.operator('sourceops.pose_bone_transforms(type="ROTATION")', text="Relative Rotaion")
            col.operator('valve.proceduralbone')'''

        row = col.row(align=True)
        row.prop(scn, 'BoneList')
        row = col.row(align=True)
        row.operator('valve.rename_bones_dict', icon='BONE_DATA')

        bst, _ = addon_utils.check("io_scene_valvesource")
        if bst:
            row = col.row()
            row.label(text="Batch Export")
            row = col.row(align=True)
            row.operator('valve.batch_export_actions', text="Action")
            row.operator('valve.batch_export_actions_retarget', text="Action Retarget")

        #row = col.row()
        #row.operator('valve.rename_biped')
        #row.operator('valve.rename_bip')
        #row.prop(scn, 'NameTemplate', icon='TEXT')
        #row.operator('valve.rename_chain')


class VIEW3D_PT_MeshTools(View3DTools, bpy.types.Panel):
    """All related options related to MESH edits, such Shape Keys"""
    #bl_idname = 'valve.mesh_panel'
    bl_label = 'Mesh tools'
    bl_parent_id = 'VIEW3D_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Most tools works for the active object")

        split = layout.split(align=True)
        col = split.column(align=True)

        row = col.row(align=True)
        row.operator('valve.createfacs')
        row.operator('valve.create_corrective_shapes', text="Create Corrective Shapes")
        bst, _ = addon_utils.check("io_scene_valvesource")
        if bst:
            col.operator('object.sourcetools_generate_corrective_drivers', text="Create Corrective Drivers")
        row.operator('mesh.clear_blank_shape_keys')

        layout.operator('red_utils.transfer_shapes')
        layout.operator('red_utils.bake_shape_ranges')
        layout.operator('red_utils.bake_shape')
        box = layout.box()
        box.prop(scn, 'ForwardAxis')
        box.prop(scn, 'SplitPower')
        box.operator('red_utils.create_stereo_split')
        box = layout.box()
        box.operator('red_utils.create_corrector_shapekey')
        box.label(text="Relative <-> Absolute")
        row = box.row()
        row.operator('red_utils.shapekey_to_relative', text="To relative")
        row.operator('red_utils.shapekey_to_absolute', text="To absolute")

class VIEW3D_PT_TextureTools(View3DTools, bpy.types.Panel):
    """All related options related to Image edits"""
    bl_idname = 'valve.texture_panel'
    bl_label = 'Texture tools'
    bl_parent_id = 'VIEW3D_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Most tools works for the active object")

        split = layout.split()
        #box = layout.box()
        col = split.column()
        row = col.row(align=True)

        row.operator("alpha.split")

class VIEW3D_PT_ShapesKeyTools(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.shape_transfer'
    bl_label = 'Transfer shapes'
    bl_parent_id = 'VIEW3D_PT_TOOLSPANEL'
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

class VIEW3D_PT_RenameTools(View3DTools, bpy.types.Panel):
    #bl_idname = 'valve.rename_panel'
    bl_label = 'Renaming tools'
    bl_parent_id = 'VIEW3D_PT_TOOLSPANEL'
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
        box.operator('valve.renamebonechain')
