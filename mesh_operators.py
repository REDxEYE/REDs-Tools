import bpy

from bpy.props import *
import numpy as np


# noinspection PyPep8Naming
class SHAPE_KEYS_OT_TransferShapes(bpy.types.Operator):
    bl_idname = "red_utils.transfer_shapes"
    bl_label = "Transfer shapes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objs = context.selected_objects
        target = context.active_object

        objs.remove(target)
        source = objs[0]

        src_vertices = np.zeros((len(source.data.vertices) * 3,), dtype=np.float32)
        source.data.vertices.foreach_get('co', src_vertices)

        dst_vertices = np.zeros((len(target.data.vertices) * 3,), dtype=np.float32)
        target.data.vertices.foreach_get('co', dst_vertices)

        for src_shape_key in source.data.shape_keys.key_blocks[1:]:
            src_shape_vertices = np.zeros((len(source.data.vertices) * 3,), dtype=np.float32)
            src_shape_key.data.foreach_get('co', src_shape_vertices)

            delta = src_shape_vertices - src_vertices
            if target.data.shape_keys.key_blocks == 0:
                target.shape_key_add(name="base")

            shape = target.shape_key_add(name=src_shape_key.name)

            shape.data.foreach_set("co", dst_vertices + delta)

        return {'FINISHED'}


class SHAPE_KEYS_OT_BakeShapeKey(bpy.types.Operator):
    bl_idname = "red_utils.bake_shape_ranges"
    bl_label = "Bake shape key min/max values"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        target = context.active_object
        active_shape_key_id = target.active_shape_key_index

        shape_key = target.data.shape_keys.key_blocks[active_shape_key_id]
        val_min = shape_key.slider_min
        val_max = shape_key.slider_max

        dst_vertices = np.zeros((len(target.data.vertices) * 3,), dtype=np.float32)
        target.data.vertices.foreach_get('co', dst_vertices)

        src_shape_vertices = np.zeros((len(target.data.vertices) * 3,), dtype=np.float32)
        shape_key.data.foreach_get('co', src_shape_vertices)

        shape = target.shape_key_add(name=shape_key.name + f"_max({val_max})")
        delta = src_shape_vertices - dst_vertices
        shape.data.foreach_set("co", dst_vertices + (delta * val_max))

        shape = target.shape_key_add(name=shape_key.name + f"_m in({val_min})")
        delta = src_shape_vertices - dst_vertices
        shape.data.foreach_set("co", dst_vertices + (delta * val_min))

        return {'FINISHED'}


class SHAPE_KEY_OT_BakeShapeKeyModifiers(bpy.types.Operator):
    bl_idname = "red_utils.bake_shape"
    bl_label = "Bake mesh with shape keys"
    bl_options = {'REGISTER', 'UNDO'}

    def get_evaluated_object(self, ob):
        depth = bpy.context.evaluated_depsgraph_get()
        return ob.evaluated_get(depth)

    def execute(self, context):
        source = context.active_object

        for shape in source.data.shape_keys.key_blocks.values():
            shape.value = 0

        dg = bpy.context.evaluated_depsgraph_get()

        mesh = bpy.data.meshes.new_from_object(source.evaluated_get(dg), preserve_all_data_layers=True, depsgraph=dg)
        name = source.name + "_baked"
        target = bpy.data.objects.new(name, mesh)
        target.shape_key_add(name='Basis')
        bpy.context.collection.objects.link(target)

        for group_name, _ in source.vertex_groups.items():
            weight_group = target.vertex_groups.get(group_name,
                                                    None) or target.vertex_groups.new(
                name=group_name)

        for key_name, key_data in source.data.shape_keys.key_blocks.items()[1:]:
            for shape in source.data.shape_keys.key_blocks.values():
                shape.value = 0

            key_data.value = 1

            key_source = self.get_evaluated_object(source)
            key_source_mesh = bpy.data.meshes.new_from_object(key_source, preserve_all_data_layers=True, depsgraph=dg)
            src_vertices = np.zeros((len(key_source_mesh.vertices) * 3,), dtype=np.float32)
            key_source_mesh.vertices.foreach_get('co', src_vertices)

            bpy.data.meshes.remove(key_source_mesh)

            shape_target = target.data.shape_keys.key_blocks.get(key_name, None) or target.shape_key_add(name=key_name)
            if target.data.shape_keys.key_blocks == 0:
                target.shape_key_add(name="base")

            shape_target.data.foreach_set("co", src_vertices)

        return {'FINISHED'}


class SHAPE_KEY_OT_CreateStereoSplit(bpy.types.Operator):
    bl_idname = "red_utils.create_stereo_split"
    bl_label = "Create stereo split"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source = context.active_object
        split_axis = context.scene.ForwardAxis
        split_power = context.scene.SplitPower
        axis_id = {"X": 0, "Y": 1, "Z": 2}[split_axis]

        src_vertices = np.zeros((len(source.data.vertices) * 3,), dtype=np.float32)
        source.data.vertices.foreach_get('co', src_vertices)
        src_vertices = src_vertices.reshape((-1, 3))
        dimm = src_vertices.max() - src_vertices.min()
        balance_width = dimm * (1 - split_power)
        balance = src_vertices[:, axis_id]
        balance = np.clip((-balance / balance_width / 2) + 0.5, 0, 1)

        weight_group = source.vertex_groups.get('__BALANCE_L',None) or source.vertex_groups.new(name='__BALANCE_L')
        for n, v in enumerate(balance):
            weight_group.add([n], v, 'REPLACE')
        weight_group = source.vertex_groups.get('__BALANCE_R', None) or source.vertex_groups.new(name='__BALANCE_R')
        for n, v in enumerate(balance):
            weight_group.add([n], 1-v, 'REPLACE')
        return {'FINISHED'}
