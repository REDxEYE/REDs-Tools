import bpy


class View3DTools:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


# noinspection PyPep8Naming
class VIEW3D_PT_ToolsPanel(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.panel'
    bl_label = 'Source engine tools'

    def draw(self, context):
        pass

# noinspection PyPep8Naming
class VIEW3D_PT_RenameTools(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.rename_panel'
    bl_label = 'Renaming tools'
    bl_parent_id = 'valve.panel'
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
    bl_parent_id = 'valve.panel'
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
class VIEW3D_PT_QcEyes(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.qc_eye_panel'
    bl_label = 'Qc eyes tools'
    bl_parent_id = 'valve.panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        row = layout.row()
        row.label(text="Target armature")
        row.prop_search(scn, "Armature", scn, "objects", text='')


        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()
        column = box.column(align=True)
        column.operator("qceyes.popup")
        column.separator()
        column.operator("create.eyedummy")
        column.operator("qceyes.generate_qc")
        column.separator()
        column = box.column()
        column.prop(scn, 'LeftEye')
        column.prop(scn, 'RightEye')
        column.prop_search(scn, 'LeftEyeMat', bpy.data, 'materials')
        column.prop_search(scn, 'RightEyeMat', bpy.data, 'materials')
        row = column.row()
        row.prop(scn, 'EyesUp')
        row.prop(scn, 'EyesDown')
        row = column.row()
        row.prop(scn, 'EyesLeft')
        row.prop(scn, 'EyesRight')
        column.prop(scn, 'AngDev')
        if scn.Armature and bpy.data.objects[scn.Armature].type == "ARMATURE":
            row = column.row()
            row.label(text="Head Bone")
            row.prop_search(scn, "HeadBone", bpy.data.objects[scn.Armature].data, "bones", text="")


# noinspection PyPep8Naming
class VIEW3D_PT_ShapesKeyTools(View3DTools, bpy.types.Panel):
    bl_idname = 'valve.shape_tools'
    bl_label = 'Shape key tools'
    bl_parent_id = 'valve.panel'
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
        box.operator('red_utils.shapekey_split_to_stereo')
        box.operator('red_utils.shapekey_merge_from_stereo')
        box = layout.box()
        box.operator('red_utils.create_corrector_shapekey')
        box.label(text="Relative <-> Absolute")
        row = box.row()
        row.operator('red_utils.shapekey_to_relative', text="To relative")
        row.operator('red_utils.shapekey_to_absolute', text="To absolute")
