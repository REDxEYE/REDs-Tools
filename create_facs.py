##############################################################
# Purpose:
#   Criar Shape Keys que são necessários para FACS.dmx
#   Essa é a lista de FACS necessários para uso desse repo
#
#  por: Davi (Debiddo) Gooz
##############################################################
# TODO: improve amount of blended shapes without hit 96 flexcontrollers
FACS = [
#  FAC Name  # FlexController
#"frame0",   # same as AU0  (disabled for my preset)
#"frame1",   # same as AU45 (disabled for my preset)
#"frame2",   # same as EM63 (disabled for my preset)
#"frame3",   # same as EM64 (disabled for my preset)
#"frame4",   # same as AU44 (disabled for my preset)
#"f00",      # same as AU0  (disabled for my preset)
#"f01",      # same as AU45 (disabled for my preset)
#"f02",      # same as EM63 (disabled for my preset)
#"f03",      # same as EM64 (disabled for my preset)
#"f04",      # same as AU44 (disabled for my preset)
 "AU0",      # baseline / default / rest
 "AU1",      # inner_brow_raiser
 "AU1AU2",   # 
 "AU1AU4",   #
 "AU2",      # outer_brow_raiser
 "AU2AU4",   #
 "AU4",      # brow_lowerer
 "AU5",      # upper_lid_raiser
 "AU6",      # cheek_raiser
 "AU7",      # lid_tightener
 "AU9",      # nose_wrinkler
 "AU10",     # sneer
#"AU10SR",   # sneer_sideway
#"AU10SL",   # sneer_sideway
 "AU11",     # nasolabial_deepener
 "AU12",     # lip_corner_puller / a mild smile
 "AU12AU25", # smile (gmod only)
 "AU13",     # cheek_puffer
 "AU14",     # dimpler
 "AU15",     # lip_corner_depressor
 "AU16",     # lower_lip_depressor
 "AU17",     # chin_raiser
 "AU17D",    # chin_raiser
 "AU18",     # lip_pucker
 "AU18Z",    # lip_pucker
 "AU20",     # lip_stretcher
#"NC21",     # neck_tightener / Platysma
 "AU22",     # lip_funneler
 "AU22Z",    # lip_funneler
#"AU23",     # lip_tightener
 "AU24",     # lip_pressor
 "AU25",     # lip_part
 "AU26",     # jaw_drop
 "AU26Z",    # jaw_drop
 "AU27",     # mouth_stretch
 "AU27Z",    # mouth_stretch
 "AU28",     # lip_suck
#"AD29",     # jaw_front
#"AD29B",    # jaw_back
 "AD30R",    # jaw_sideways
 "AD30L",    # jaw_sideways
 "AD31",     # jaw_clencher / AD31
 "AD32",     # bite / lip_bite AD32
#"AD33",     # lip_blow
#"AD34",     # lip_snort
#"AD35",     # cheek_suck
 "AU38",     # dilator / nose_dilator
#"AU39",     # contract / nose_contract
#"GB40",     # sniff
 "AU41",     # lid_droop
#"AU42",     # lid_slit
#"AU43",     # lid_closer
 "AU44",     # lid_squint
 "AU45",     # lid_closer / blink
#"AU46",     # eye_wink
#"EM61",     # eye_turn_left
#"EM62",     # eye_turn_right
 "EM63",     # eye_turn_up
 "EM64",     # eye_turn_down
#"GB80",     # neck_swallow
#"GB81",     # neck_chew
#"AU90",     # tongue_up
#"AU91",     # tongue_down
#"AU92",     # tongue_to_left
#"AU93",     # tongue_to_right
#"AU94",     # tongue_curl
#"AU95",     # tongue_bend
 "AD96R",    # mouth_sideways
 "AD96L"     # mouth_sideways
#"AU96",     # tongue_retraction
#"AU97",     # tongue_darting_out
#"AU98",     # tongue_protrusion
#"AU99",     # tongue_twist 
#"AU100",    # tongue_rolling / styloglossus
#"AU101",    # tongue_flattening / vertical
#"TM101",    # tongue_inside_left
#"TM102",    # tongue_inside_right
#"TM103",    # tongue_outter
#"TM104",    # tongue_outside_left
#"TM105",    # tongue_outside_right
#"TM106",    # tongue_outside_up
#"TM107",    # tongue_outside_down
#"TM108",    # tongue_inside_roll_up
#"TM109",    # tongue_inside_roll_down
#"TM110",    # tongue_inner_roll_up
#"TM111",    # tongue_outter_roll_up
#"TM112",    # tongue_outter_up
#"TM113",    # tongue_outter_down
#"TM114",    # tongue_outter_concave
#"TM115",    # tongue_bite
]

import bpy

class VALVE_OT_CreateFACS(bpy.types.Operator):
    """Create minimal FACs shapes used by Debiddo's shape / flex preset"""
    bl_idname = "valve.createfacs"
    bl_label = "Create FACs shapes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = bpy.context.active_object
        if obj.type == 'MESH':
                if obj.data.shape_keys is None:
                        obj.shape_key_add(name="baseline")

                for Actor in FACS:
                        print(Actor)
                        obj.shape_key_add(name=Actor)

        return {'FINISHED'}
