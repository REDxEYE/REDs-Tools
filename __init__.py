import bpy

from bpy.props import *

from . import ValvePanel
from . import rename_bones
from .TextureTools import split_alpha

bl_info = {
    "name": "RED's Tools",
    "author": "RED_EYE",
    "version": (0, 3),
    "blender": (2, 79, 0),
    "description": "Tools for preparing armature for Source Engine export",
    # 'warning': 'May crash blender',
    # "wiki_url": "http://www.barneyparker.com/blender-json-import-export-plugin",
    # "tracker_url": "http://www.barneyparker.com/blender-json-import-export-plugin",
    "category": "Tools"
}
import importlib

importlib.reload(rename_bones)
importlib.reload(ValvePanel)

name_formats = [
    ("BIP", "Bip", "", 0),
    ("VALVEBIPED", "Valvebiped", "", 1),
]
bone_chains = [
    ('LARM', 'Left collar-hand chain', "", 0),
    ('RARM', 'Right collar-hand chain', "", 1),
    ('LLEG', 'Left hip-toe chain', "", 2),
    ('RLEG', 'Right hip-toe chain', "", 3),
    ('LTUMB', 'Left thumb finger', "", 4),
    ('RTUMB', 'Right thumb finger', "", 5),
    ('LINDX', 'Left index finger', "", 6),
    ('RINDX', 'Right index finger', "", 7),
    ('LMIDL', 'Left middle finger', "", 8),
    ('RMIDL', 'Right middle finger', "", 9),
    ('LRNG', 'Left ring finger', "", 10),
    ('RRNG', 'Right ring finger', "", 11),
    ('LPNK', 'Left pinky finger', "", 12),
    ('RPNK', 'Right pinky finger', "", 13),

]


class AlphaSplit(bpy.types.Operator):
    """Extracts alpha to new file"""
    bl_idname = "alpha.split"
    bl_label = "Split alpha"
    bl_options = {'UNDO'}

    def execute(self, context):
        sima = context.space_data
        ima = sima.image
        split_alpha(ima)
        return {'FINISHED'}


def get_bonechain_id(val):
    for a in bone_chains:
        if a[0] == val:
            return a[-1]


def split_alpha_menu(self, context):
    self.layout.operator(AlphaSplit.bl_idname, text='Split alpha')


def register():
    bpy.types.Scene.NameTemplate = StringProperty(name="Bone template", default='bip_bone_{1}')
    bpy.types.Scene.LeftEye = FloatVectorProperty(name="Left eye")
    bpy.types.Scene.RightEye = FloatVectorProperty(name="Right eye")
    bpy.types.Scene.Armature = bpy.props.StringProperty(
        name='Armature',
        description='Main armature',
    )
    bpy.types.Scene.HeadBone = bpy.props.StringProperty(
        name='Head Bone'
    )
    bpy.types.Scene.LeftEyeMat = bpy.props.StringProperty(
        name='Left Eye Material'
    )
    bpy.types.Scene.RightEyeMat = bpy.props.StringProperty(
        name='Right Eye Material'
    )
    bpy.types.Scene.NameFormat = bpy.props.EnumProperty(name="Name format", items=name_formats)
    bpy.types.Scene.BoneChains = bpy.props.EnumProperty(name="Bone chain", items=bone_chains)
    bpy.types.Scene.EyesUp = bpy.props.FloatProperty(name="Up eyes max", min=0, max=360)
    bpy.types.Scene.EyesDown = bpy.props.FloatProperty(name="Down eyes max", min=0, max=360)
    bpy.types.Scene.EyesRight = bpy.props.FloatProperty(name="Right eyes max", min=0, max=360)
    bpy.types.Scene.EyesLeft = bpy.props.FloatProperty(name="Left eyes max", min=0, max=360)
    bpy.types.Scene.AngDev = bpy.props.FloatProperty(name="Angle of deviation from center", min=-50, max=50)

    bpy.utils.register_class(rename_bones.RenameButtonBip)
    bpy.utils.register_class(rename_bones.RenameButtonValveBiped)
    bpy.utils.register_class(rename_bones.RenamePanel)
    bpy.utils.register_class(rename_bones.RenameChainButton)
    bpy.utils.register_class(rename_bones.ConnectBones)
    bpy.utils.register_class(ValvePanel.ValvePanel)
    bpy.utils.register_class(ValvePanel.CreateEyeDummys)
    bpy.utils.register_class(ValvePanel.QCEyesPopup)
    bpy.utils.register_class(ValvePanel.CleanBones)
    bpy.utils.register_class(ValvePanel.CleanBonesConstraints)
    bpy.utils.register_class(ValvePanel.RenameBoneChains)
    bpy.utils.register_class(ValvePanel.RenameChainPopup)
    bpy.utils.register_class(ValvePanel.QCEyesQCGenerator)
    bpy.utils.register_class(AlphaSplit)
    bpy.types.IMAGE_MT_image.append(split_alpha_menu)


def unregister():
    del bpy.types.Scene.NameTemplate
    del bpy.types.Scene.LeftEye
    del bpy.types.Scene.RightEye
    del bpy.types.Scene.Armature
    del bpy.types.Scene.HeadBone
    del bpy.types.Scene.LeftEyeMat
    del bpy.types.Scene.RightEyeMat
    del bpy.types.Scene.NameFormat
    del bpy.types.Scene.BoneChains
    del bpy.types.Scene.EyesUp
    del bpy.types.Scene.EyesDown
    del bpy.types.Scene.EyesRight
    del bpy.types.Scene.EyesLeft
    del bpy.types.Scene.AngDev
    bpy.utils.unregister_class(rename_bones.RenameButtonBip)
    bpy.utils.unregister_class(rename_bones.RenameButtonValveBiped)
    bpy.utils.unregister_class(rename_bones.RenamePanel)
    bpy.utils.unregister_class(rename_bones.RenameChainButton)
    bpy.utils.unregister_class(rename_bones.ConnectBones)
    bpy.utils.unregister_class(ValvePanel.ValvePanel)
    bpy.utils.unregister_class(ValvePanel.CreateEyeDummys)
    bpy.utils.unregister_class(ValvePanel.QCEyesPopup)
    bpy.utils.unregister_class(ValvePanel.CleanBones)
    bpy.utils.unregister_class(ValvePanel.CleanBonesConstraints)
    bpy.utils.unregister_class(ValvePanel.RenameBoneChains)
    bpy.utils.unregister_class(ValvePanel.RenameChainPopup)
    bpy.utils.unregister_class(ValvePanel.QCEyesQCGenerator)
    bpy.utils.unregister_class(AlphaSplit)
    bpy.types.IMAGE_MT_image.remove(split_alpha_menu)


if __name__ == "__main__":
    register()
