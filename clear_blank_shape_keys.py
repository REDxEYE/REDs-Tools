##########################################
# Purpose:
#   Delete unused Shape Keys of the selected Objects
#   for a cleaner workflow
##########################################

import bpy
import numpy as np
from .operators import enable_if

# Tolerance to small differences, change it if you want
tolerance = 0.00001

class MESH_OT_clear_blank_shape_keys(bpy.types.Operator):
    """batch exports all Actions into its own file.
    use with Blender Source Tools"""
    bl_idname = "mesh.clear_blank_shape_keys"
    bl_label = "Remove Blank Shape Keys"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        enable_if(context, 'MESH')

    def execute(self, context):
        assert context.mode == 'OBJECT', "Must be in object mode!"

        for ob in context.selected_objects:
            # allow search over all selected objects but iterate only with MESH
            if ob.type != 'MESH': continue
            if not ob.data.shape_keys: continue
            if not ob.data.shape_keys.use_relative: continue

            kbs = ob.data.shape_keys.key_blocks
            nverts = len(ob.data.vertices)
            to_delete = []

            # Cache locs for rel keys since many keys have the same rel key
            cache = {}

            locs = np.empty(3*nverts, dtype=np.float32)

            for kb in kbs:
                if kb == kb.relative_key: continue

                kb.data.foreach_get("co", locs)

                if kb.relative_key.name not in cache:
                    rel_locs = np.empty(3*nverts, dtype=np.float32)
                    kb.relative_key.data.foreach_get("co", rel_locs)
                    cache[kb.relative_key.name] = rel_locs
                rel_locs = cache[kb.relative_key.name]

                locs -= rel_locs
                if (np.abs(locs) < tolerance).all():
                    to_delete.append(kb.name)

            for kb_name in to_delete:
                ob.shape_key_remove(ob.data.shape_keys.key_blocks[kb_name])
