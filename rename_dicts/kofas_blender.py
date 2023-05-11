################################################################################
# Purpose:
#   Rename Bones (The King of Fighters: All-Stars) to a Blender friendly names
#
# Usage:
#	Select an armature imported form asset from The King of Fighters: All-Stars
#	Select the armature and run this script, all bones renamed to their a Blender Friendly counterparts
################################################################################

names = dict()

#names['Ch_Chunli_SFV']     = 'Ch_Chunli_SFV'
#names['Ch_Chunli_Cos_SFV'] = 'Ch_Chunli_Cos_SFV'
#names['Ch_SolBadGuy_GGX']  = 'Ch_SolBadGuy_GGX'
#names['Translate']         = 'Translate'
#names['Bip001']            = 'Bip001'

names['Bip001 Pelvis'] = 'Spine'
names['Bip001 Spine']  = 'Spine1'
names['Bip001 Spine1'] = 'Spine4'
names['Bip001 Neck']   = 'Neck1'
names['Bip001 Head']   = 'Head1'

names['Bip001 L Finger0']  = 'Finger0_L'
names['Bip001 L Finger01'] = 'Finger01_L'
names['Bip001 L Finger02'] = 'Finger02_L'
names['Bip001 L Finger1']  = 'Finger1_L'
names['Bip001 L Finger11'] = 'Finger11_L'
names['Bip001 L Finger12'] = 'Finger12_L'
names['Bip001 L Finger2']  = 'Finger2_L'
names['Bip001 L Finger21'] = 'Finger21_L'
names['Bip001 L Finger22'] = 'Finger22_L'
names['Bip001 L Finger3']  = 'Finger3_L'
names['Bip001 L Finger31'] = 'Finger31_L'
names['Bip001 L Finger32'] = 'Finger32_L'
names['Bip001 L Finger4']  = 'Finger4_L'
names['Bip001 L Finger41'] = 'Finger41_L'
names['Bip001 L Finger42'] = 'Finger42_L'

names['Bip001 R Finger0']  = 'Finger0_R'
names['Bip001 R Finger01'] = 'Finger01_R'
names['Bip001 R Finger02'] = 'Finger02_R'
names['Bip001 R Finger1']  = 'Finger1_R'
names['Bip001 R Finger11'] = 'Finger11_R'
names['Bip001 R Finger12'] = 'Finger12_R'
names['Bip001 R Finger2']  = 'Finger2_R'
names['Bip001 R Finger21'] = 'Finger21_R'
names['Bip001 R Finger22'] = 'Finger22_R'
names['Bip001 R Finger3']  = 'Finger3_R'
names['Bip001 R Finger31'] = 'Finger31_R'
names['Bip001 R Finger32'] = 'Finger32_R'
names['Bip001 R Finger4']  = 'Finger4_R'
names['Bip001 R Finger41'] = 'Finger41_R'
names['Bip001 R Finger42'] = 'Finger42_R'

names['Bip001 L Clavicle'] = 'Clavicle_L'
names['Bip001 L UpperArm'] = 'UpperArm_L'
names['Bip001 L Forearm']  = 'Forearm_L'
names['Bip001 L Hand']     = 'Hand_L'

names['Bip001 R Clavicle'] = 'Clavicle_R'
names['Bip001 R UpperArm'] = 'UpperArm_R'
names['Bip001 R Forearm']  = 'Forearm_R'
names['Bip001 R Hand']     = 'Hand_R'

names['Bip001 L Thigh'] = 'Thigh_L'
names['Bip001 L Calf']  = 'Calf_L'
names['Bip001 L Foot']  = 'Foot_L'
names['Bip001 L Toe0']  = 'Toe0_L'

names['Bip001 R Thigh'] = 'Thigh_R'
names['Bip001 R Calf']  = 'Calf_R'
names['Bip001 R Foot']  = 'Foot_R'
names['Bip001 R Toe0']  = 'Toe0_R'

# Procedural bones/ helper bones
names['Bone_R Clavicle']       = 'Helper_Shoulder_L'      # NOTE: bone have their names inverted
names['Bone L Soulder Twist']  = 'Helper_Shoulder_L'
names['Bone_L_Shoulder']       = 'Helper_Shoulder_L'
names['Bone L UpperArm']       = 'Helper_UpperArmTwist_L'
names['Bone_UpperArm_Tw_L']    = "Helper_UpperArmTwist_L"
names['Bone L UpperArm Twist'] = 'Helper_UpperArm_L'
names['Bip001_B_L Elbow']      = 'Helper_Elbow_L'
names['Bip001 L ForeTwist']    = 'Helper_Ulna_L'
names['Bip001 L ForeTwist1']   = 'Helper_Wrist_L'

names['Bone_L Clavicle']       = 'Helper_Shoulder_R'      # NOTE: bone have their names inverted
names['Bone R Soulder Twist']  = 'Helper_Shoulder_R'
names['Bone_R_Shoulder']       = 'Helper_Shoulder_R'
names['Bone R UpperArm']       = 'Helper_UpperArmTwist_R'
names['Bone_UpperArm_Tw_R']    = "Helper_UpperArmTwist_R"
names['Bone R UpperArm Twist'] = 'Helper_UpperArm_R'
names['Bip001_B_R Elbow']      = 'Helper_Elbow_R'
names['Bip001 R ForeTwist']    = 'Helper_Ulna_R'
names['Bip001 R ForeTwist1']   = 'Helper_Wrist_R'

names['Bone_L_hip']          = 'Helper_Hip_L'
names['Bone_L_Hip']          = 'Helper_Hip_L'
names['Bip001 LThighTwist']  = 'Helper_Quadricep_L'
names['Bip001 L ThighTwist'] = 'Helper_Quadricep_L'
names['Bone_L_knee']         = 'Helper_Knee_L'
names['Bip001_B_L Hip']      = 'Helper_Glute_L'

names['Bone_R_hip']          = 'Helper_Hip_R'
names['Bone_R_Hip']          = 'Helper_Hip_R'
names['Bip001 RThighTwist']  = 'Helper_Quadricep_R'
names['Bip001 R ThighTwist'] = 'Helper_Quadricep_R'
names['Bone_R_knee']         = 'Helper_Knee_R'
names['Bip001_B_R Hip']      = 'Helper_Glute_R'

# jiggles and additional bones per skin
names['Bone_L_Acc'] = 'Acc_End_L'
names['Bip001 Xtra_L_Acc'] = 'Acc_L'
names['Bip001 Xtra_L_Acc02'] = 'Acc02_L'
names['Bip001 Xtra_L_Acc03'] = 'Acc03_L'
names['Bip001 Xtra_R_Acc_CosOpp'] = 'Acc_Cos_L'
names['Bip001 Xtra_R_Acc_CosOpp02'] = 'Acc_Cos02_L'
names['Bip001 Xtra_R_Acc_CosOpp03'] = 'Acc_Cos03_L'
names['Bip001 Xtra_R_Acc_CosOpp04'] = 'Acc_Cos04_L'

names['Bone_R_Acc'] = 'Acc_End_R'
names['Bip001 Xtra_R_Acc'] = 'Acc_R'
names['Bip001 Xtra_R_Acc03'] = 'Acc03_R'
names['Bip001 Xtra_R_Acc02'] = 'Acc02_R'
names['Bip001 Xtra_R_Acc_Cos'] = 'Acc_Cos_R'
names['Bip001 Xtra_R_Acc_Cos02'] = 'Acc_Cos02_R'
names['Bip001 Xtra_R_Acc_Cos03'] = 'Acc_Cos03_R'
names['Bip001 Xtra_R_Acc_Cos04'] = 'Acc_Cos04_R'

names['Bip001 Xtra_hair'] = 'Hair'

# female characters have uncommon breast names
names['Bone_Bu_L'] = 'Breast_L'       # actual jiggle
names['Bone_Bu_R'] = 'Breast_R'       # actual jiggle

names['Point009'] = 'Breast'          # dummy shit to attach objects in Unity
names['Point015'] = 'Helper_Breast'   # center control
names['Point007'] = 'Helper_Breast_L' # left procedural fixup
names['Point010'] = 'Helper_Breast_R' # right procedural fixup

# clothes jiggles
names['Bip001 Xtra_RB_Skt03'] = 'B_Skt03_R'
names['Bip001 Xtra_RB_Skt02'] = 'B_Skt02_R'
names['Bip001 Xtra_LB_Skt02'] = 'B_Skt02_L'
names['Bip001 Xtra_RB_Skt']   = 'B_Skt_R'
names['Bip001 Xtra_RF_Skt']   = 'F_Skt_R'
names['Bip001 Xtra_LF_Skt04'] = 'F_Skt04_L'
names['Bip001 Xtra_RF_Skt02'] = 'F_Skt02_R'
names['Bip001 Xtra_LF_Skt']   = 'F_Skt_L'
names['Bip001 Xtra_LB_Skt05'] = 'B_Skt05_L'
names['Bip001 Xtra_RB_Skt05'] = 'B_Skt05_R'
names['Bip001 Xtra_LF_Skt03'] = 'F_Skt03_L'
names['Bip001 Xtra_LF_Skt02'] = 'F_Skt02_L'
names['Bip001 Xtra_LB_Skt03'] = 'B_Skt03_L'
names['Bip001 Xtra_LB_Skt04'] = 'B_Skt04_L'
names['Bip001 Xtra_RF_Skt03'] = 'F_Skt03_R'
names['Bip001 Xtra_RB_Skt04'] = 'B_Skt04_R'
names['Bip001 Xtra_RF_Skt04'] = 'F_Skt04_R'
names['Bip001 Xtra_LB_Skt']   = 'B_Skt_L'

# dummy reference animation attachments
names['Bone_L_Eye'] = 'lefteye'
names['Bone_R_Eye'] = 'righteye'
names['Bip001 Xtra_Eye_Ctrl'] = 'Eye_Ctrl'

# Solbadguy Belt
names['Bip001 Belt01'] = 'Helper_Belt01'
names['Bip001 Belt02'] = 'Helper_Belt02'

names['Bip001 Belt01_ L01'] = 'Helper_Belt01_L'   # NOTE: sim tem um espaço e por isso é diferente do lado oposto
names['Bip001 Belt01_L02']  = 'Belt01_02_L'
names['Bip001 Belt01_L03']  = 'Belt01_03_L'
names['Bip001 Belt01_R01']  = 'Helper_Belt01_R'
names['Bip001 Belt01_R02']  = 'Belt01_02_R'
names['Bip001 Belt01_R03']  = 'Belt01_03_R'

names['Bone_Ankle_Belt_L'] = 'Ankle_Belt_L'
names['Bone_Ankle_Belt_R'] = 'Ankle_Belt_R'

names['Bip001 Collar B Upper'] = 'CollarBack'
names['Bip001 Collar L Down']  = 'CollarDown_L'
names['Bip001 Collar L Upper'] = 'CollarUp_L'
names['Bip001 Collar R Down']  = 'CollarDown_R'
names['Bip001 Collar R Upper'] = 'CollarUp_R'

names['Bone_Hair_B']   = 'Hair_B'
names['Bone_Hair_F']   = 'Hair_F'
names['Bone_Hair_FD']  = 'Hair_FD'
names['Bone_Hair_FRD'] = 'Hair_FRD'
names['Bone_Hair_LD']  = 'Hair_LD'
names['Bone_Hair_M']   = 'Hair_M'
names['Bone_Hair_R']   = 'Hair_R'
names['Bone_Hair_RD']  = 'Hair_RD'

names['Bone_HairRibbon_L_01'] = 'Hair_Ribbon_L_01'
names['Bone_HairRibbon_L_01'] = 'Hair_Ribbon_L_01'
names['Bone_HairRibbon_R_01'] = 'Hair_Ribbon_R_01'
names['Bone_HairRibbon_R_02'] = 'Hair_Ribbon_R_02'

names['Bone_PonyTail_M_01'] = 'PonyTail01_M'
names['Bone_PonyTail_M_02'] = 'PonyTail02_M'
names['Bone_PonyTail_M_03'] = 'PonyTail03_M'
names['Bone_PonyTail_M_04'] = 'PonyTail04_M'
names['Bone_PonyTail_M_05'] = 'PonyTail05_M'
names['Bone_PonyTail_L_01'] = 'PonyTail01_L'
names['Bone_PonyTail_L_02'] = 'PonyTail02_L'
names['Bone_PonyTail_R_01'] = 'PonyTail01_R'
names['Bone_PonyTail_R_02'] = 'PonyTail02_R'
names['Bone_PonyTail_U_01'] = 'PonyTail01_U'
names['Bone_PonyTail_U_02'] = 'PonyTail02_U'

