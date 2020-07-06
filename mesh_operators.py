import bpy

from bpy.props import *
import numpy as np


# noinspection PyPep8Naming
class TransferShapes(bpy.types.Operator):
    bl_idname = "red_utils.transfer_shapes"
    bl_label = "Transfer shapes"
    bl_options = {'REGISTER', 'UNDO'}

    def pool(self, context):
        return len(context.selected_objects) == 2

    def execute(self, context):
        objs = context.selected_objects

        source, target = objs

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


class BakeShapeKey(bpy.types.Operator):
    bl_idname = "red_utils.bake_shape"
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

        if val_max != 1.0:
            shape = target.shape_key_add(name=shape_key.name + f"_max({val_max})")
            delta = src_shape_vertices - dst_vertices
            shape.data.foreach_set("co", dst_vertices + (delta * val_max))

        if val_min != 0.0:
            shape = target.shape_key_add(name=shape_key.name + f"_max({val_min})")
            delta = src_shape_vertices - dst_vertices
            shape.data.foreach_set("co", dst_vertices + (delta * val_min))
