import bpy

import mathutils
from bpy.props import *

try:
    from . import bone_table
except ImportError:
    import bone_table


class RenamePanel(bpy.types.Panel):
    bl_idname = "Armature.SourceEngineTools"
    bl_label = "Source Engine armature tools"

    bl_options = {'DEFAULT_CLOSED'}
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.type == 'ARMATURE')

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        row = layout.row()
        column = row.column()
        column.operator("rename.biped")
        column = row.column()
        column.operator("rename.bip")
        row = layout.row()
        column = row.column()
        column.prop(scn, 'NameTemplate')
        column = row.column()
        column.operator('rename.chain')
        row = layout.row()
        row.operator('armature.connect')


class RenameButtonValveBiped(bpy.types.Operator):
    bl_idname = "rename.biped"
    bl_label = "Convert to ValveBiped"

    def execute(self, context):
        o = context.object
        if (o.select and o.type == 'ARMATURE'):
            for name, bone in o.data.bones.items():
                if name in bone_table.bone_table_bip:
                    bone.name = bone_table.bone_table_valvebiped[name]
        return {'FINISHED'}


class RenameButtonBip(bpy.types.Operator):
    bl_idname = "rename.bip"
    bl_label = "Convert to Bip"

    def execute(self, context):
        o = context.object
        if (o.select and o.type == 'ARMATURE'):
            for name, bone in o.data.bones.items():
                if name in bone_table.bone_table_bip:
                    bone.name = bone_table.bone_table_bip[name]
            for bone in context.selected_pose_bones:
                if not bone.name.lower().startswith('bip_'):
                    left = None
                    new_name = 'bip_'
                    num = None
                    temp_name = bone.name  # type: str
                    temp_name = temp_name.replace('.', '_')
                    if temp_name.lower().endswith('l'):
                        left = True
                        temp_name = temp_name[:-2]
                    elif temp_name.lower().endswith('r'):
                        left = False
                        temp_name = temp_name[:-2]
                    if temp_name[-3:].isnumeric():
                        try:
                            num = int(temp_name[-3:])
                            temp_name = temp_name[:-4]
                        except:
                            num = None
                    new_name += temp_name
                    if num != None:
                        new_name += '_' + str(num)
                    if left != None:
                        if left:
                            new_name += '_L'
                        else:
                            new_name += '_R'
                    bone.name = new_name

        return {'FINISHED'}


class RenameChainButton(bpy.types.Operator):
    bl_idname = "rename.chain"
    bl_label = "Rename chain of bones"

    def execute(self, context):
        o = context.object
        if (o.select and o.type == 'ARMATURE'):
            for b, bone in enumerate(context.selected_pose_bones):
                n = 0
                if "{1}" in context.scene.NameTemplate or "{0}" in context.scene.NameTemplate:
                    bone.name = context.scene.NameTemplate.format(b, n)
                else:
                    bone.name = context.scene.NameTemplate.format(n)
                while bone.children:
                    n += 1
                    bone = bone.children[0]
                    if "{1}" in context.scene.NameTemplate or "{0}" in context.scene.NameTemplate:
                        bone.name = context.scene.NameTemplate.format(b, n)
                    else:
                        bone.name = context.scene.NameTemplate.format(n)
        return {'FINISHED'}


class ConnectBones(bpy.types.Operator):
    bl_idname = "armature.connect"
    bl_label = "Connect bones"

    def execute(self, context):
        o = context.object
        bpy.ops.object.mode_set(mode='EDIT')
        for bone_ in context.selected_editable_bones:

            if bone_.parent:
                parent = bone_.parent
                if len(parent.children) > 1:
                    bone_.use_connect = False
                    parent.tail = sum([ch.head for ch in parent.children], mathutils.Vector()) / len(parent.children)
                else:
                    parent.tail = bone_.head
                    bone_.use_connect = True
                    if bone_.children == 0:
                        par = bone_.parent
                        if par.children > 1:
                            pass
                        bone_.tail = bone_.head + (par.tail - par.head)
                    if not bone_.parent and bone_.children > 1:
                        bone_.tail = (bone_.head + bone_.tail) * 2
                if bone_.head == parent.head:
                    print(bone_.name)
                    bone_.tail = parent.tail
                elif not bone_.children:
                    vec = bone_.parent.head - bone_.head
                    bone_.tail = bone_.head - vec / 2

        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z')
        bpy.ops.object.mode_set(mode='POSE')
        return {'FINISHED'}
