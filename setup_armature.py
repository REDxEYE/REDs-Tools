##############################################################
# Purpose:
#   Define layers específicas que combinam com meu workflow
#
#  por: Davi (Debiddo) Gooz
##############################################################
import bpy
from .operators import enable_if, is_mode, get_edit_bone

# import common bone lists
from .bone_lists.bones_valve import bones as bones_valve
from .bone_lists.bones_helpers import bones as bones_helpers
from .bone_lists.bones_mmdbase import bones as bones_mmdbase
from .bone_lists.bones_breast import bones as bones_breast
from .bone_lists.bones_attachments import bones as bones_attachments
from .bone_lists.bones_facials import bones as bones_facials

from .bone_lists.bones_tx import bones as bones_tx
from .bone_lists.bones_without_deform import bones as bones_no_deform
from .bone_lists.bones_more import bones as bones_more

from .bone_lists.bones_bad import bones as bones_bad

# Character Specific
from .bone_lists.bones_aponia import bones_aponia, bone_aponia_tip, aponia_lingering

prefix_valve = "ValveBiped.Bip01_"
prefix_helpers = "Helper_"
group_valvebiped = 0
group_helpers = 1
group_jiggle = 2
group_attachments = 3

layer_valve = 0
layer_helpers = 1
layer_breast = 2
layer_hair = 3
layer_cloth = 4
layer_attachments = 16


def bone_control(lista, deform=True, control=True):
    '''Isso só funciona se em POSE Mode
    
    Nota: bones com o deform desligado não são exportados e sua hierarquia não é resolvida.'''
    is_mode('OBJECT', 'OBJECT')
    for bone in lista:
        selected = get_edit_bone(bone)
        if (selected):
            selected.select = control
            selected.use_deform = deform


def set_bone_layer(lista, bone_layer, bool):
    '''isso só funciona se em OBJECT Mode'''
    is_mode('POSE', 'POSE')
    for bone in [bones for bones in bpy.context.object.data.bones]:
        if bone.name in lista:
            bone.layers[bone_layer] = bool


def iterate_bone_layers(lista, layer):
    '''Manda o bones de lista para a layer declarada e remove das demais layers. 
    - layer: é a layer que o bone deve permanecer. (default: 31)

    obs: range(32) é porque o range é de 0 à 31'''
    for n in range(32):
        if n == layer:
            set_bone_layer(lista, n, True)
        else:
            set_bone_layer(lista, n, False)


class ARMATURE_OT_SetupBones(bpy.types.Operator):
    """Enforce Bones layers and deforms"""
    bl_idname = "valve.setup_bones_layers"
    bl_label = "Valve Setup Bones"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')

    def execute(self, context):
        # organize lyers
        bone_control(bones_no_deform, False)
        iterate_bone_layers(bones_no_deform, 31)
        iterate_bone_layers(bones_attachments, layer_attachments)
        iterate_bone_layers(bones_helpers, layer_helpers)
        iterate_bone_layers(bones_valve, layer_valve)
        #iterate_bone_layers(bones_aponia, layer_hair)
        iterate_bone_layers(bones_breast, layer_breast)
        iterate_bone_layers(bones_facials, 19)

        return {'FINISHED'}


''' TODO: sanitize os shapes com caracters proibidos
Closer>< = iconclose
hips     = hips
Breasts  = Breasts
'''