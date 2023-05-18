import bpy

from bpy.props import *

from . import texture_tools
from . import tools_panel
from . import rename_bones
from . import operators
from . import mesh_operators
from . import qc_eyes

bl_info = {
    "name": "RED's Tools",
    "author": "RED_EYE, Davi (Debiddo) Gooz",
    "version": (1, 4),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Tool",
    "description": "Multi-purpose tools preparing armature for Source Engine export",
    'warning': '',
    'wiki_url': 'https://github.com/REDxEYE/REDs-Tools/wiki',
    "category": "Tool"
}
import importlib

importlib.reload(rename_bones)
importlib.reload(tools_panel)

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

eyelid_format = [
    ("dmxeyelid", "DMX", "Use DMX file for eyelid shapes (recommended)", 0),
    ("eyelid", "VTA", "Use VTA file for eyelid shapes (deprecated)", 1),
]

forward_axis = [
    ("X", "X", "", 0),
    ("Y", "Y", "", 1),
    ("Z", "Z", "", 2),
]


class IMAGE_MT_AlphaSplit(bpy.types.Operator):
    """Extracts alpha to new file"""
    bl_idname = "alpha.split"
    bl_label = "Split alpha"
    bl_options = {'UNDO'}

    def execute(self, context):
        sima = context.space_data
        ima = sima.image
        texture_tools.split_alpha(ima)
        return {'FINISHED'}


def get_bonechain_id(val):
    for a in bone_chains:
        if a[0] == val:
            return a[-1]


def split_alpha_menu(self, context):
    self.layout.operator(IMAGE_MT_AlphaSplit.bl_idname, text='Split alpha')


classes = [
    mesh_operators.SHAPE_KEYS_OT_TransferShapes,
    mesh_operators.SHAPE_KEYS_OT_BakeShapeKey,
    mesh_operators.SHAPE_KEY_OT_BakeShapeKeyModifiers,
    mesh_operators.SHAPE_KEY_OT_CreateStereoSplit,

    rename_bones.BONE_OT_RenameButtonBip,
    rename_bones.BONE_OT_RenameButtonValveBiped,
    rename_bones.BONE_PT_RenamePanel,
    rename_bones.BONE_OT_RenameChainButton,
    rename_bones.BONE_OT_ConnectBones,
    rename_bones.BONE_OT_MergeBones,

    tools_panel.VIEW3D_PT_ToolsPanel,
    tools_panel.VIEW3D_PT_ArmatureTools,
    tools_panel.VIEW3D_PT_RenameTools,
    tools_panel.VIEW3D_PT_TrasnferShapes,

    # qc_eyes will have a dedicated section
    qc_eyes.VALVE_PT_QcEyes,
    qc_eyes.VALVE_OT_UpdateDepsGraphEyeDummies,
    qc_eyes.VALVE_OT_CreateEyeDummies,
    qc_eyes.VALVE_OT_QCEyesQCGenerator,
    qc_eyes.VALVE_OT_QCEyesPopup,

    operators.BONES_OT_CleanBones,
    operators.BONES_OT_CleanBonesConstraints,
    operators.BONES_OT_RenameBoneChains,
    operators.BONES_OT_RenameChainPopup,
    operators.BONES_OT_QCEyesQCGenerator,
    operators.BONES_TP_CompareArmatures,


    IMAGE_MT_AlphaSplit
]
register_, unregister_ = bpy.utils.register_classes_factory(classes)


def register():
    bpy.types.Scene.NameTemplate = bpy.props.StringProperty(name="", default='bip_bone_{1}')
    bpy.types.Scene.LeftEye = bpy.props.FloatVectorProperty(name="Left eye")
    bpy.types.Scene.RightEye = bpy.props.FloatVectorProperty(name="Right eye")
    bpy.types.Scene.Armature = bpy.props.StringProperty(
        name='Armature',
        description='Main armature',
    )
    bpy.types.Scene.HeadBone = bpy.props.StringProperty(name='Head Bone')
    bpy.types.Scene.LeftEyeMat = bpy.props.StringProperty(name='Left Eye Material')
    bpy.types.Scene.RightEyeMat = bpy.props.StringProperty(name='Right Eye Material')
    bpy.types.Scene.NameFormat = bpy.props.EnumProperty(name="Name format", items=name_formats)
    bpy.types.Scene.BoneChains = bpy.props.EnumProperty(name="Bone chain", items=bone_chains)
    bpy.types.Scene.EyesUp = bpy.props.FloatProperty(description='Eyes Up / Down min value', name="min", min=-180, max=0)
    bpy.types.Scene.EyesDown = bpy.props.FloatProperty(description='Eyes Up / Down max value', name="max", min=0, max=180)
    bpy.types.Scene.EyesLeft = bpy.props.FloatProperty(description='Eyes Left / Right min value', name="min", min=-180, max=0)
    bpy.types.Scene.EyesRight = bpy.props.FloatProperty(description='Eyes Left / Right max value', name="max", min=0, max=180)
    bpy.types.Scene.AngDev = bpy.props.FloatProperty(name='Deviation Angle', description="Angle of deviation from center", min=-50, max=50)

    bpy.types.Scene.HeadObject = bpy.props.StringProperty(name='Object Name',description='Head Object name')
    bpy.types.Scene.UpperLower = bpy.props.FloatProperty(name='Upper Lid Lowerer', description='DmxEyelid: Upper Lid Lowerer location')
    bpy.types.Scene.UpperNeutral = bpy.props.FloatProperty(name='Upper Lid Neutral', description='DmxEyelid: Upper Lid Neutral location')
    bpy.types.Scene.UpperRaiser = bpy.props.FloatProperty(name='Upper Lid Raiser', description='DmxEyelid: Upper Lid Raiser location')
    bpy.types.Scene.LowerLowerer = bpy.props.FloatProperty(name='Lower Lid Lowerer', description='DmxEyelid: Lower Lid Lowerer location')
    bpy.types.Scene.LowerNeutral = bpy.props.FloatProperty(name='Lower Lid Neutral', description='DmxEyelid: Lower Lid Neutral location')
    bpy.types.Scene.LowerRaiser = bpy.props.FloatProperty(name='Lower Lid Raiser', description='DmxEyelid: Lower Lid Raiser location')

    bpy.types.Scene.EyeFormats = bpy.props.EnumProperty(name="Eyelid Format", items=eyelid_format)

    bpy.types.Scene.ForwardAxis = bpy.props.EnumProperty(name="Forward axis", items=forward_axis)
    bpy.types.Scene.SplitPower = bpy.props.FloatProperty(name="Split power", min=0, max=1, default=0.995, precision=4)

    register_()

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
    del bpy.types.Scene.HeadObject
    del bpy.types.Scene.UpperLower
    del bpy.types.Scene.UpperNeutral
    del bpy.types.Scene.UpperRaiser
    del bpy.types.Scene.LowerLowerer
    del bpy.types.Scene.LowerNeutral
    del bpy.types.Scene.LowerRaiser
    del bpy.types.Scene.EyeFormat
    del bpy.types.Scene.ForwardAxis
    del bpy.types.Scene.SplitPower
    unregister_()


if __name__ == "__main__":
    register()
