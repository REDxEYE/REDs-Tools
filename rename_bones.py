import bpy

import mathutils
from bpy.props import *

try:
    from . import bone_table
except ImportError:
    import bone_table


class BONE_PT_RenamePanel(bpy.types.Panel):
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


class BONE_OT_RenameButtonValveBiped(bpy.types.Operator):
    bl_idname = "rename.biped"
    bl_label = "Convert to ValveBiped"

    def execute(self, context):
        o = context.object
        if (o.select_get() and o.type == 'ARMATURE'):
            for name, bone in o.data.bones.items():
                if name in bone_table.bone_table_bip:
                    bone.name = bone_table.bone_table_valvebiped[name]
        return {'FINISHED'}


class BONE_OT_RenameButtonBip(bpy.types.Operator):
    bl_idname = "rename.bip"
    bl_label = "Convert to Bip"

    def execute(self, context):
        o = context.object
        if (o.select_get() and o.type == 'ARMATURE'):
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


class BONE_OT_RenameChainButton(bpy.types.Operator):
    bl_idname = "rename.chain"
    bl_label = "Rename chain of bones"

    def execute(self, context):
        o = context.object
        if o.select_get() and o.type == 'ARMATURE':
            for b, bone in enumerate(context.selected_pose_bones_from_active_object):
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


class BONE_OT_ConnectBones(bpy.types.Operator):
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


class BONE_OT_MergeBones(bpy.types.Operator):
    bl_idname = "armature.merge"
    bl_label = "Merge bones"

    def delete_bone_and_transfer_weights(self, armature, bone_to_delete, target_bone):
        if armature.type != 'ARMATURE':
            print(f"Armature '{armature}' is not armature!")
            return

        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        old_mirror_state = bpy.context.object.data.use_mirror_x
        bpy.context.object.data.use_mirror_x = False

        if bone_to_delete not in armature.data.edit_bones:
            print(f"Bone '{bone_to_delete}' not found in armature!")
            return

        if target_bone not in armature.data.edit_bones:
            print(f"Target bone '{target_bone}' not found in armature!")
            return

        bpy.context.object.data.use_mirror_x = old_mirror_state
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                for mod in obj.modifiers.values():
                    if mod.type == "ARMATURE" and mod.object == armature:
                        if obj.name not in bpy.context.view_layer.objects:
                            continue
                        bpy.context.view_layer.objects.active = obj
                        bpy.ops.object.mode_set(mode='OBJECT')

                        vg_delete = obj.vertex_groups.get(bone_to_delete)
                        vg_target = obj.vertex_groups.get(target_bone)

                        if vg_delete and vg_target:
                            for vertex in obj.data.vertices:
                                for group in vertex.groups:
                                    if group.group == vg_delete.index:
                                        weight_to_transfer = group.weight
                                        vg_target.add([vertex.index], weight_to_transfer, 'ADD')

                            obj.vertex_groups.remove(vg_delete)

        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        armature.data.edit_bones.remove(armature.data.edit_bones[bone_to_delete])

        bpy.ops.object.mode_set(mode='OBJECT')
        print(f"Bone '{bone_to_delete}' deleted and weights transferred to '{target_bone}'.")

    def execute(self, context):
        this = context.active_pose_bone
        others = list(filter(lambda a: a != this, context.selected_pose_bones))
        arm = this.id_data
        arm_name = arm.name
        for other in others:
            self.delete_bone_and_transfer_weights(arm, other.name, this.name)
        bpy.context.view_layer.objects.active = bpy.data.objects[arm_name]
        bpy.ops.object.mode_set(mode='POSE')
        return {'FINISHED'}


class BONE_OT_CollapseBones(bpy.types.Operator):
    bl_idname = "armature.collapse"
    bl_label = "Collapse one bone into another"

    def delete_bone_and_transfer_weights(self, armature, bone_to_delete, target_bone):
        if armature.type != 'ARMATURE':
            print(f"Armature '{armature}' is not armature!")
            return

        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        old_mirror_state = bpy.context.object.data.use_mirror_x
        bpy.context.object.data.use_mirror_x = False

        if bone_to_delete not in armature.data.edit_bones:
            print(f"Bone '{bone_to_delete}' not found in armature!")
            return

        if target_bone not in armature.data.edit_bones:
            print(f"Target bone '{target_bone}' not found in armature!")
            return
        bpy.context.object.data.use_mirror_x = old_mirror_state
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                for mod in obj.modifiers.values():
                    if mod.type == "ARMATURE" and mod.object == armature:
                        if obj.name not in bpy.context.view_layer.objects:
                            continue
                        bpy.context.view_layer.objects.active = obj
                        bpy.ops.object.mode_set(mode='OBJECT')

                        vg_delete = obj.vertex_groups.get(bone_to_delete)
                        vg_target = obj.vertex_groups.get(target_bone)

                        if vg_delete and vg_target:
                            for vertex in obj.data.vertices:
                                for group in vertex.groups:
                                    if group.group == vg_delete.index:
                                        weight_to_transfer = group.weight
                                        vg_target.add([vertex.index], weight_to_transfer, 'ADD')

                            obj.vertex_groups.remove(vg_delete)

        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        armature.data.edit_bones.remove(armature.data.edit_bones[bone_to_delete])

        bpy.ops.object.mode_set(mode='OBJECT')
        print(f"Bone '{bone_to_delete}' deleted and weights transferred to '{target_bone}'.")

    def execute(self, context):
        old_mirror_state = bpy.context.object.data.use_mirror_x
        bpy.context.object.data.use_mirror_x = False

        this = context.active_pose_bone
        this_name = this.name
        other = next(filter(lambda a: a != this, context.selected_pose_bones), None)
        other_tail = other.tail.copy()
        if other is None:
            self.report({'WARNING'}, "Select at least two bones")
            return {'CANCELLED'}
        arm = this.id_data
        arm_name = arm.name
        self.delete_bone_and_transfer_weights(arm, other.name, this.name)

        bpy.context.view_layer.objects.active = arm
        bpy.ops.object.mode_set(mode='EDIT')

        arm.data.edit_bones[this_name].tail = other_tail

        bpy.context.view_layer.objects.active = bpy.data.objects[arm_name]
        bpy.ops.object.mode_set(mode='POSE')
        bpy.context.object.data.use_mirror_x = old_mirror_state

        return {'FINISHED'}
