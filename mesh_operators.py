import bpy

from bpy.props import *
import numpy as np


# noinspection PyPep8Naming
class TrasferShapes(bpy.types.Operator):
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

            shape = target.shape_key_add(name=src_shape_key.name)

            shape.data.foreach_set("co", dst_vertices + delta)

        return {'FINISHED'}
