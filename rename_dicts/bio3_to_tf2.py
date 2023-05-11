
# Purpose: select an armature on a human model imported form Bio3
# run this script, all bones renamed to their TF2 counterparts

names = dict()
 
# Purpose: select an armature from a Bio3 model
# run this
# Get a TF2 style armature

names['GenericHumanPelvis'] = 'bip_pelvis'
names['GenericHumanSpine1'] = 'bip_spine_0'
names['GenericHumanSpine2'] = 'bip_spine_1'
names['GenericHumanSpine3'] = 'bip_spine_2'
names['GenericHumanRibcage'] = 'bip_spine_3'
names['GenericHumanNeck'] = 'bip_neck'
names['GenericHumanHead'] = 'bip_head'
 
names['GenericHumanRCollarbone'] = 'bip_collar_R'
names['GenericHumanLCollarbone'] = 'bip_collar_L'
 
names['GenericHumanRUpperarm1'] = 'bip_upperArm_R'
names['GenericHumanRForearm1'] = 'bip_lowerArm_R'
names['GenericHumanRPalm'] = 'bip_hand_R'
names['GenericHumanRUpperarm2'] = 'hlp_upperArm_R'
names['GenericHumanRForearm2'] = 'hlp_lowerArm_R'
 
names['GenericHumanRDigit11'] = 'bip_thumb_0_R'
names['GenericHumanRDigit12'] = 'bip_thumb_1_R'
names['GenericHumanRDigit13'] = 'bip_thumb_2_R'
 
names['GenericHumanRDigit21'] = 'bip_index_0_R'
names['GenericHumanRDigit22'] = 'bip_index_1_R'
names['GenericHumanRDigit23'] = 'bip_index_2_R'
 
names['GenericHumanRDigit31'] = 'bip_middle_0_R'
names['GenericHumanRDigit32'] = 'bip_middle_1_R'
names['GenericHumanRDigit33'] = 'bip_middle_2_R'
 
names['GenericHumanRDigit41'] = 'bip_ring_0_R'
names['GenericHumanRDigit42'] = 'bip_ring_1_R'
names['GenericHumanRDigit43'] = 'bip_ring_2_R'
 
names['GenericHumanRDigit51'] = 'bip_pinky_0_R'
names['GenericHumanRDigit52'] = 'bip_pinky_1_R'
names['GenericHumanRDigit53'] = 'bip_pinky_2_R'
 
names['GenericHumanRThigh'] = 'bip_hip_R'
names['GenericHumanRCalf'] = 'bip_knee_R'
names['GenericHumanRFoot'] = 'bip_foot_R'
names['GenericHumanRToe1'] = 'bip_toe_R'
 
names['GenericHumanDressBone_FR1'] = 'prp_dress_r01_1'
names['GenericHumanDressBone_FR2'] = 'prp_dress_r01_2'
names['GenericHumanDressBone_FR3'] = 'prp_dress_r01_3'
names['GenericHumanDressBone_FR4'] = 'prp_dress_r01_4'
names['GenericHumanDressBone_FR5'] = 'prp_dress_r01_5'
 
names['GenericHumanDressBone_R1'] = 'prp_dress_r02_1'
names['GenericHumanDressBone_R2'] = 'prp_dress_r02_2'
names['GenericHumanDressBone_R3'] = 'prp_dress_r02_3'
names['GenericHumanDressBone_R4'] = 'prp_dress_r02_4'
names['GenericHumanDressBone_R5'] = 'prp_dress_r02_5'
 
names['GenericHumanDressBone_BR1'] = 'prp_dress_r03_1'
names['GenericHumanDressBone_BR2'] = 'prp_dress_r03_2'
names['GenericHumanDressBone_BR3'] = 'prp_dress_r03_3'
names['GenericHumanDressBone_BR4'] = 'prp_dress_r03_4'
names['GenericHumanDressBone_BR5'] = 'prp_dress_r03_5'
 
names['GenericHumanLUpperarm1'] = 'bip_upperArm_L'
names['GenericHumanLForearm1'] = 'bip_lowerArm_L'
names['GenericHumanLPalm'] = 'bip_hand_L'
names['GenericHumanLUpperarm2'] = 'hlp_upperArm_L'
names['GenericHumanLForearm2'] = 'hlp_lowerArm_L'
 
names['GenericHumanLDigit11'] = 'bip_thumb_0_L'
names['GenericHumanLDigit12'] = 'bip_thumb_1_L'
names['GenericHumanLDigit13'] = 'bip_thumb_2_L'
 
names['GenericHumanLDigit21'] = 'bip_index_0_L'
names['GenericHumanLDigit22'] = 'bip_index_1_L'
names['GenericHumanLDigit23'] = 'bip_index_2_L'
 
names['GenericHumanLDigit31'] = 'bip_middle_0_L'
names['GenericHumanLDigit32'] = 'bip_middle_1_L'
names['GenericHumanLDigit33'] = 'bip_middle_2_L'
 
names['GenericHumanLDigit41'] = 'bip_ring_0_L'
names['GenericHumanLDigit42'] = 'bip_ring_1_L'
names['GenericHumanLDigit43'] = 'bip_ring_2_L'
 
names['GenericHumanLDigit51'] = 'bip_pinky_0_L'
names['GenericHumanLDigit52'] = 'bip_pinky_1_L'
names['GenericHumanLDigit53'] = 'bip_pinky_2_L'
 
names['GenericHumanLThigh'] = 'bip_hip_L'
names['GenericHumanLCalf'] = 'bip_knee_L'
names['GenericHumanLFoot'] = 'bip_foot_L'
names['GenericHumanLToe1'] = 'bip_toe_L'
 
names['GenericHumanDressBone_FL1'] = 'prp_dress_l01_1'
names['GenericHumanDressBone_FL2'] = 'prp_dress_l01_2'
names['GenericHumanDressBone_FL3'] = 'prp_dress_l01_3'
names['GenericHumanDressBone_FL4'] = 'prp_dress_l01_4'
names['GenericHumanDressBone_FL5'] = 'prp_dress_l01_5'
 
names['GenericHumanDressBone_L1'] = 'prp_dress_l02_1'
names['GenericHumanDressBone_L2'] = 'prp_dress_l02_2'
names['GenericHumanDressBone_L3'] = 'prp_dress_l02_3'
names['GenericHumanDressBone_L4'] = 'prp_dress_l02_4'
names['GenericHumanDressBone_L5'] = 'prp_dress_l02_5'
 
names['GenericHumanDressBone_BL1'] = 'prp_dress_l03_1'
names['GenericHumanDressBone_BL2'] = 'prp_dress_l03_2'
names['GenericHumanDressBone_BL3'] = 'prp_dress_l03_3'
names['GenericHumanDressBone_BL4'] = 'prp_dress_l03_4'
names['GenericHumanDressBone_BL5'] = 'prp_dress_l03_5'

names['GenericHumanBreathingBone'] = 'hlp_chestbreath'

names['GenericHuman_BackHair01'] = 'bip_hair_b1'
names['GenericHuman_BackHair02'] = 'bip_hair_b2'
names['GenericHuman_BackHair03'] = 'bip_hair_b3'
names['GenericHuman_BackHair04'] = 'bip_hair_b4'
names['GenericHuman_BackHair05'] = 'bip_hair_b5'

names['GenericHuman_PonyTail01'] = 'bip_hair_b3'
names['GenericHuman_PonyTail02'] = 'bip_hair_b4'
names['GenericHuman_PonyTail03'] = 'bip_hair_b5'

names['GenericHuman_RHair01'] = 'bip_hair_1r'
names['GenericHuman_RHair02'] = 'bip_hair_2r'

names['GenericHuman_LHair01'] = 'bip_hair_1l'
names['GenericHuman_LHair02'] = 'bip_hair_2l'

names['GenericHuman_FrontHair01'] = 'bip_hair_fb1'
names['GenericHuman_FrontHair02'] = 'bip_hair_fb2'

names['GenericHuman_RFaceHair01'] = 'bip_hair_fa1'
names['GenericHuman_RFaceHair02'] = 'bip_hair_fa2'
names['GenericHuman_RFaceHair03'] = 'bip_hair_fa3'

names['GenericHuman_LFaceHair01'] = 'bip_hair_fc1'
names['GenericHuman_LFaceHair02'] = 'bip_hair_fc2'
names['GenericHuman_LFaceHair03'] = 'bip_hair_fc3'

names['R_Grip'] = 'weapon_bone'
names['L_Grip'] = 'weapon_bone_L'

