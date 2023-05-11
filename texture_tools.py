import bpy
from pathlib import Path

import numpy as np

def split_alpha(blender_texture):
    image_data = np.array(blender_texture.pixels)
    alpha_view = image_data[3::4]
    alpha = alpha_view.copy()
    alpha = np.repeat(alpha, 4)
    alpha[3::4][:] = 1
    alpha_im = bpy.data.images.new(Path(blender_texture.name).stem + '_A', width=blender_texture.size[0],
                                   height=blender_texture.size[1])
    alpha_im.pixels = alpha
    alpha_im.pack(as_png=True)
    alpha_view[:] = 1
    blender_texture.pixels = image_data

def split_alpha_menu(self, context):
    self.layout.operator(IMAGE_MT_AlphaSplit.bl_idname, text='Split alpha')

class IMAGE_MT_AlphaSplit(bpy.types.Operator):
    """Extracts alpha to new file"""
    bl_idname = "alpha.split"
    bl_label = "Split alpha"
    bl_options = {'UNDO'}

    def execute(self, context):
        sima = context.space_data
        ima = sima.image
        split_alpha(ima)
        return {'FINISHED'}
