################################################################################
# Purpose:
#   Rename Bones (Fortnite) to a Blender friendly names
#
# Usage:
#	Select an armature imported form asset from Fortnite
#	Select the armature and run this script, all bones renamed to their a Blender Friendly counterparts
################################################################################

names = dict()
names['pelvis']       = 'Pelvis'
names['abdomenLower'] = 'Spine'
names['abdomenUpper'] = 'Spine1'
names['chestLower']   = 'Spine2'
names['chestUpper']   = 'Spine4'
names['neckLower']    = 'Neck1'
names['neckUpper']    = 'Head1'

names['lThumb1'] = 'Finger0_L'
names['lThumb2'] = 'Finger01_L'
names['lThumb3'] = 'Finger02_L'
names['lIndex1'] = 'Finger1_L'
names['lIndex2'] = 'Finger11_L'
names['lIndex3'] = 'Finger12_L'
names['lMid1']   = 'Finger2_L'
names['lMid2']   = 'Finger21_L'
names['lMid3']   = 'Finger22_L'
names['lRing1']  = 'Finger3_L'
names['lRing2']  = 'Finger31_L'
names['lRing3']  = 'Finger32_L'
names['lPinky1'] = 'Finger4_L'
names['lPinky2'] = 'Finger41_L'
names['lPinky3'] = 'Finger42_L'

names['rThumb1'] = 'Finger0_R'
names['rThumb2'] = 'Finger01_R'
names['rThumb3'] = 'Finger02_R'
names['rIndex1'] = 'Finger1_R'
names['rIndex2'] = 'Finger11_R'
names['rIndex3'] = 'Finger12_R'
names['rMid1']   = 'Finger2_R'
names['rMid2']   = 'Finger21_R'
names['rMid3']   = 'Finger22_R'
names['rRing1']  = 'Finger3_R'
names['rRing2']  = 'Finger31_R'
names['rRing3']  = 'Finger32_R'
names['rPinky1'] = 'Finger4_R'
names['rPinky2'] = 'Finger41_R'
names['rPinky3'] = 'Finger42_R'

names['lCollar']      = 'Clavicle_L'
names['lShldrBend']   = 'UpperArm_L'
names['lForearmBend'] = 'Forearm_L'
names['lHand']        = 'Hand_L'

names['rCollar']      = 'Clavicle_R'
names['rShldrBend']   = 'UpperArm_R'
names['rForearmBend'] = 'Forearm_R'
names['rHand']        = 'Hand_R'

names['lThighBend']   = 'Thigh_L'
names['lShin']        = 'Calf_L'
names['lFoot']        = 'Foot_L'
names['lMetatarsals'] = 'Toe0_L'

names['rThighBend']   = 'Thigh_R'
names['rShin']        = 'Calf_R'
names['rFoot']        = 'Foot_R'
names['rMetatarsals'] = 'Toe0_R'

# Procedural bones/ helper bones
#names[''] = 'Helper_Shoulder_L'
names['lShldrTwist'] = 'Helper_UpperArmTwist_L'
#names[''] = 'Helper_UpperArm_L'
#names[''] = 'Helper_Elbow_L'
#names[''] = 'Helper_Ulna_L'
names['lForearmTwist'] = 'Helper_Wrist_L'

#names[''] = 'Helper_Shoulder_R'
names['rShldrTwist'] = "Helper_UpperArmTwist_R"
#names[''] = 'Helper_UpperArm_R'
#names[''] = 'Helper_Elbow_R'
#names[''] = 'Helper_Ulna_R'
names['rForearmTwist'] = 'Helper_Wrist_R'

#names[''] = 'Helper_Hip_L'
#names[''] = 'Helper_Hip_L'
names['lThighTwist'] = 'Helper_Quadricep_L'
#names[''] = 'Helper_Knee_L'
#names[''] = 'Helper_Glute_L'

#names[''] = 'Helper_Hip_R'
#names[''] = 'Helper_Hip_R'
names['rThighTwist'] = 'Helper_Quadricep_R'
#names[''] = 'Helper_Knee_R'
#names[''] = 'Helper_Glute_R'

# breast
names['rPectoral'] = 'Breast_L'
names['lPectoral'] = 'Breast_R'

# Dummy?
#names['Genesis8Female'] = ''
#names['GoldenPalace_Shell'] = ''
#names['GoldenPalace_Shell.]Shape' = ''
#names['GoldenPalace_2254'] = ''
#names['GoldenPalace_2254.]Shape' = ''

#names['hip'] = ''

# Face related
#names['head'] = ''
#names['upperFaceRig'] = ''
#names['R_lip_upper_outer'] = ''
#names['teeth_upper'] = ''
#names['L_eye'] = ''
#names['L_eye_lid_lower_mid'] = ''
#names['L_eye_lid_upper_mid'] = ''
#names['R_eye_lid_lower_mid'] = ''
#names['R_eye_lid_upper_mid'] = ''
#names['C_jaw'] = ''
#names['tongue'] = ''
#names['teeth_lower'] = ''
#names['R_lip_lower_outer'] = ''
#names['C_lip_lower_mid'] = ''
#names['L_lip_lower_outer'] = ''
#names['R_lip_corner'] = ''
#names['R_cheek_inner'] = ''
#names['R_brow_outer'] = ''
#names['R_brow_mid'] = ''
#names['C_nose_bridge'] = ''
#names['L_lip_corner'] = ''
#names['L_lip_upper_outer'] = ''
#names['C_lip_upper_mid'] = ''
#names['L_cheek_inner'] = ''
#names['L_brow_outer'] = ''
#names['L_brow_mid'] = ''
#names['C_brow_mid'] = ''

# jigglebones (Hair)
#names['dyn_hair_08'] = ''
#names['dyn_hair_07'] = ''
#names['dyn_hair_06'] = ''
#names['dyn_hair_05'] = ''
#names['dyn_hair_04'] = ''
#names['dyn_hair_03'] = ''
#names['dyn_hair_02'] = ''
#names['dyn_hair_01'] = ''
#names['dyn_ear_01_l'] = ''
#names['dyn_ear_02_l'] = ''
#names['dyn_ear_01_r'] = ''
#names['dyn_ear_02_r'] = ''
#names['dyn_hair_02_r'] = ''
#names['dyn_hair_02_l'] = ''
#names['dyn_hair_02_b'] = ''
#names['dyn_hair_01_t'] = ''
#names['dyn_hair_01_r'] = ''
#names['dyn_hair_01_l'] = ''
#names['dyn_hair_01_f'] = ''
#names['dyn_hair_01_b'] = ''

# Hands Procedurals
names['lCarpal4'] = 'Carpal4_L'
names['lCarpal3'] = 'Carpal3_L'
names['lCarpal2'] = 'Carpal2_L'
names['lCarpal1'] = 'Carpal1_L'

names['rCarpal4'] = 'Carpal4_R'
names['rCarpal3'] = 'Carpal3_R'
names['rCarpal2'] = 'Carpal2_R'
names['rCarpal1'] = 'Carpal1_R'

# NSFW female part
#names['Clitoris'] = ''
#names['Vagina'] = ''
#names['Rectum'] = ''
#names['Colon'] = ''

names['lLabiumMajora1']     = 'LabiumMajora1_L'
names['lLabiumMajora2']     = 'LabiumMajora2_L'
names['Left Small Labia 1'] = 'Small_Labia_1_L'
names['Left Small Labia 2'] = 'Small_Labia_2_L'
names['Left Small Labia 3'] = 'Small_Labia_3_L'
names['Left Small Labia 4'] = 'Small_Labia_4_L'

names['rLabiumMajora1']      = 'LabiumMajora1_R'
names['rLabiumMajora2']      = 'LabiumMajora2_R'
names['Right Small Labia1' ] = 'Small_Labia1__R'
names['Right Small Labia 2'] = 'Small_Labia_2_R'
names['Right Small Labia 3'] = 'Small_Labia_3_R'
names['Right Small Labia 4'] = 'Small_Labia_4_R'

# feets (likely for procedurals))
names['lToe']         = 'Toe_L'
names['lBigToe']      = 'BigToe_L'
names['lBigToe_2']    = 'BigToe_2_L'
names['lSmallToe1']   = 'SmallToe1_L'
names['lSmallToe1_2'] = 'SmallToe1_2_L'
names['lSmallToe2']   = 'SmallToe2_L'
names['lSmallToe2_2'] = 'SmallToe2_2_L'
names['lSmallToe3']   = 'SmallToe3_L'
names['lSmallToe3_2'] = 'SmallToe3_2_L'
names['lSmallToe4']   = 'SmallToe4_L'
names['lSmallToe4_2'] = 'SmallToe4_2_L'

names['rToe']         = 'Toe_R'
names['rBigToe']      = 'BigToe_R'
names['rBigToe_2']    = 'BigToe_2_R'
names['rSmallToe1']   = 'SmallToe1_R'
names['rSmallToe1_2'] = 'SmallToe1_2_R'
names['rSmallToe2']   = 'SmallToe2_R'
names['rSmallToe2_2'] = 'SmallToe2_2_R'
names['rSmallToe3']   = 'SmallToe3_R'
names['rSmallToe3_2'] = 'SmallToe3_2_R'
names['rSmallToe4']   = 'SmallToe4_R'
names['rSmallToe4_2'] = 'SmallToe4_2_R'
