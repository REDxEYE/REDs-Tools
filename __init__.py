import bpy

#from bpy.props import __all__

#from . import texture_tools
from . import tools_panel
from . import operators
#from . import mesh_operators
from . import selected_bones
from . import create_facs
from . import copy_pose
from . import qc_eyes
from . import batch_smd_export
from . import empty_to_bones
from . import copy_procedural
from . import setup_armature
from . import clear_blank_shape_keys

# from lists import *

bl_info = {
    "name": "Source Engine Tools",
    "author": "RED_EYE, Davi (Debiddo) Gooz",
    "version": (1, 5),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Tool",
    "description": "Multi-purpose tools for preparing armature for Source Engine export, derivated from the deprecated RED Tool's",
    'warning': '',
    'wiki_url': 'https://github.com/LoveRenamon/REDs-Tools/wiki',
    "category": "Tool"
}

bone_dict = [ # Esse dici existe para selecionar qual dicionário para renomear bones
    ("blender_valve",    "Blender to ValveBiped",                      "Rename from: Blender\nto: ValveBiped Format", 0),
    ("valve_blender",    "ValveBiped to Blender",                      "Rename from: ValveBiped\nto: Blender Format", 1),
    ("dscs_to_blender",  "Digimon Story: CyberSleuth to Blender",      "Rename from: Digimon Story: CyberSleuth\nto: Blender Format", 2),
    ("rxd_blender",      "Rockman X-DiVE to Blender",                  "Rename from: Rockman X-DiVE\nto: Blender Format", 3),
    ("rigfy_blender",    "Rigfy to Blender",                           "Rename from: Rigfy\nto: Blender Format", 4),
    ("mmd_valvebiped",   "MMD to ValveBiped",                          "Rename from: MMD\nto: ValveBiped Format", 5),
    ("kofas_blender",    "The King of Fighters: All-Stars to Blender", "Rename from: The King of Fighters: All-Stars\nto: Blender Format", 6),
    ("fortnite_blender", "Fortnite to Blender",                        "Rename from: Fortnite\nto: Blender Format", 7),
    ("tf2_blender",      "Team Fortress 2 to Blender",                 "Rename from: Team Fortress 2\nto: Blender Format", 8),
    ("bio3_tf2",         "Bioshock 3 to Team Fortress 2",              "Rename from: Bioshock 3\nto: Team Fortress 2 Format", 9),
]
forward_axis = [
    ("X", "X", "", 0),
    ("Y", "Y", "", 1),
    ("Z", "Z", "", 2),
]


classes = [
    # mesh_operators.SHAPE_KEYS_OT_TransferShapes,
    # mesh_operators.SHAPE_KEYS_OT_BakeShapeKey,
    # mesh_operators.SHAPE_KEY_OT_BakeShapeKeyModifiers,
    # mesh_operators.SHAPE_KEY_OT_CreateStereoSplit,

    operators.VALVE_OT_ConnectBones,
    operators.VALVE_OT_MergeBoneWeights,

    operators.VALVE_OT_CleanBonesShape,
    operators.VALVE_OT_RenameBonesTo,
    operators.ARMATURE_OT_LockBoneLocation,
    operators.ARMATURE_OT_SetBoneViewMode,
    operators.ARMATURE_OT_SetBoneHierarchy,

    tools_panel.VALVE_PT_ToolsPanel,
    tools_panel.VALVE_PT_MeshTools,
    tools_panel.VALVE_PT_ArmatureTools,
    #tools_panel.VALVE_PT_TextureTools,
    #tools_panel.VALVE_PT_TrasnferShapes,
    #tools_panel.VALVE_PT_RenameTools,

    # qc_eyes tem uma secção dedicada
    qc_eyes.VALVE_PT_QcEyes,
    qc_eyes.VALVE_OT_UpdateDepsGraphEyeDummies,
    qc_eyes.VALVE_OT_CreateEyeDummies,
    qc_eyes.VALVE_OT_QCEyesQCGenerator,
    qc_eyes.VALVE_OT_QCEyesPopup,

    selected_bones.ARMATURE_OT_WeightBonesClipboard,
    selected_bones.ARMATURE_OT_SelectedBonesClipboard,
    selected_bones.ARMATURE_OT_SelectedBonesBonemergeClipboard,

    # Isso é relacionado ao meu workflow pessoal
    copy_pose.VALVE_OT_CopyPose,
    create_facs.VALVE_OT_CreateFACS,
    batch_smd_export.VALVE_OT_BatchExportActions,
    batch_smd_export.VALVE_OT_BatchExportActionsRetarget,
    copy_procedural.VALVE_OT_ProceduralBone,
    setup_armature.ARMATURE_OT_SetupBones,
    empty_to_bones.ARMATURE_OT_empty_to_armature,
    clear_blank_shape_keys.MESH_OT_clear_blank_shape_keys,

    #texture_tools.IMAGE_MT_AlphaSplit
]
register_, unregister_ = bpy.utils.register_classes_factory(classes)


def register():
    #bpy.types.Scene.NameTemplate = bpy.props.StringProperty(name="", default='bip_bone_{1}')
    bpy.types.Scene.LeftEye = bpy.props.FloatVectorProperty(name="Left Eye")
    bpy.types.Scene.RightEye = bpy.props.FloatVectorProperty(name="Right Eye")
    bpy.types.Scene.Armature = bpy.props.StringProperty(
        name='Armature',
        description='Main armature',
    )

    bpy.types.Scene.BoneList = bpy.props.EnumProperty(
        name="Bone list",
        description='Select which dictionary we\'ll use',
        items=bone_dict,
    )

    bpy.types.Scene.HeadBone = bpy.props.StringProperty(name='Head Bone')
    bpy.types.Scene.LeftEyeMat = bpy.props.StringProperty(name='Left Eye Material')
    bpy.types.Scene.RightEyeMat = bpy.props.StringProperty(name='Right Eye Material')
    #bpy.types.Scene.NameFormat = bpy.props.EnumProperty(name="Name format", items=name_formats)
    #bpy.types.Scene.BoneChains = bpy.props.EnumProperty(name="Bone chain", items=bone_chains)
    bpy.types.Scene.EyesUp = bpy.props.FloatProperty(name="Up eyes max", min=0, max=360)
    bpy.types.Scene.EyesDown = bpy.props.FloatProperty(name="Down eyes max", min=0, max=360)
    bpy.types.Scene.EyesRight = bpy.props.FloatProperty(name="Right eyes max", min=0, max=360)
    bpy.types.Scene.EyesLeft = bpy.props.FloatProperty(name="Left eyes max", min=0, max=360)
    bpy.types.Scene.AngDev = bpy.props.FloatProperty(name="Angle of deviation from center", min=-50, max=50)

    bpy.types.Scene.HeadObject = bpy.props.StringProperty(name='Object Name',description='Head Object name')
    bpy.types.Scene.UpperLower = bpy.props.FloatProperty(name='Upper Lid Lowerer', description='DmxEyelid: Upper Lid Lowerer location')
    bpy.types.Scene.UpperNeutral = bpy.props.FloatProperty(name='Upper Lid Neutral', description='DmxEyelid: Upper Lid Neutral location')
    bpy.types.Scene.UpperRaiser = bpy.props.FloatProperty(name='Upper Lid Raiser', description='DmxEyelid: Upper Lid Raiser location')
    bpy.types.Scene.LowerLowerer = bpy.props.FloatProperty(name='Lower Lid Lowerer', description='DmxEyelid: Lower Lid Lowerer location')
    bpy.types.Scene.LowerNeutral = bpy.props.FloatProperty(name='Lower Lid Neutral', description='DmxEyelid: Lower Lid Neutral location')
    bpy.types.Scene.LowerRaiser = bpy.props.FloatProperty(name='Lower Lid Raiser', description='DmxEyelid: Lower Lid Raiser location')

    bpy.types.Scene.ForwardAxis = bpy.props.EnumProperty(name="Forward axis", items=forward_axis)
    bpy.types.Scene.SplitPower = bpy.props.FloatProperty(name="Split power", min=0, max=1, default=0.995, precision=4)

    register_()

    #bpy.types.IMAGE_MT_image.append(split_alpha_menu)


def unregister():
    #del bpy.types.Scene.NameTemplate
    del bpy.types.Scene.LeftEye
    del bpy.types.Scene.RightEye
    del bpy.types.Scene.Armature
    del bpy.types.Scene.HeadBone
    del bpy.types.Scene.LeftEyeMat
    del bpy.types.Scene.RightEyeMat
    del bpy.types.Scene.BoneList
    #del bpy.types.Scene.NameFormat
    #del bpy.types.Scene.BoneChains
    del bpy.types.Scene.EyesUp
    del bpy.types.Scene.EyesDown
    del bpy.types.Scene.EyesRight
    del bpy.types.Scene.EyesLeft
    del bpy.types.Scene.AngDev
    del bpy.types.Scene.ForwardAxis
    del bpy.types.Scene.HeadObject
    del bpy.types.Scene.UpperLower
    del bpy.types.Scene.UpperNeutral
    del bpy.types.Scene.UpperRaiser
    del bpy.types.Scene.LowerLowerer
    del bpy.types.Scene.LowerNeutral
    del bpy.types.Scene.LowerRaiser
    unregister_()


if __name__ == "__main__":
    register()
