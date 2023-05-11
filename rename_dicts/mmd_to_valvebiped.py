
# Purpose: select an armature on a human model imported form Left 4 Dead, Garry's Mode, Half-Life 2
# run this script, all bones renamed to their VaveBiped counterparts

names = dict()

# Purpose: select an armature from a MMD model
# run this
# Get a VaveBiped style armature

names['Hip'] = 'ValveBiped.Bip01_Pelvis'
names['Spine'] = 'ValveBiped.Bip01_Spine'
names['Spine0'] = 'ValveBiped.Bip01_Spine0'
names['Spine1'] = 'ValveBiped.Bip01_Spine1'
names['Spine2'] = 'ValveBiped.Bip01_Spine2'
names['Spine3'] = 'ValveBiped.Bip01_Spine3'
names['Spine4'] = 'ValveBiped.Bip01_Spine4'
names['LowerBody'] = 'ValveBiped.Bip01_Spine'
names['UpperBody'] = 'ValveBiped.Bip01_Spine0'
#names[''] = 'ValveBiped.Bip01_Spine1'
#names[''] = 'ValveBiped.Bip01_Spine2'
#names[''] = 'ValveBiped.Bip01_Spine3'
names['UpperBody2'] = 'ValveBiped.Bip01_Spine4'

names['Neck'] = 'ValveBiped.Bip01_Neck1'
names['Head'] = 'ValveBiped.Bip01_Head1'

#names[''] = 'Helper_Hip_R'
#names[''] = 'Helper_Hip_L'
#names[''] = 'Helper_Glute_R'
#names[''] = 'Helper_Glute_L'
#names[''] = 'Helper_Sartorius_R'
#names[''] = 'Helper_Sartorius_L'
names['LegD_R'] = 'ValveBiped.Bip01_R_Thigh'
names['LegD_L'] = 'ValveBiped.Bip01_L_Thigh'
names['LeftLegD'] = 'ValveBiped.Bip01_L_Thigh'
names['RightLegD'] = 'ValveBiped.Bip01_R_Thigh'
#names[''] = 'Helper_Quadricep_R'
#names[''] = 'Helper_Quadricep_L'
#names[''] = 'Helper_Quad_R'
#names[''] = 'Helper_Quad_L'
#names[''] = 'Helper_Knee_R'
#names[''] = 'Helper_Knee_L'
names['KneeD_R'] = 'ValveBiped.Bip01_R_Calf'
names['KneeD_L'] = 'ValveBiped.Bip01_L_Calf'
names['RightKneeD'] = 'ValveBiped.Bip01_R_Calf'
names['LeftKneeD'] = 'ValveBiped.Bip01_L_Calf'
#names[''] = 'Helper_Shin_R'
#names[''] = 'Helper_Shin_L'
#names[''] = 'Helper_Soleus_R'
#names[''] = 'Helper_Soleus_L'
#names[''] = 'Helper_Ankle_R'
#names[''] = 'Helper_Ankle_L'
names['AnkleD_R'] = 'ValveBiped.Bip01_R_Foot'
names['AnkleD_L'] = 'ValveBiped.Bip01_L_Foot'
names['RightAnkleD'] = 'ValveBiped.Bip01_R_Foot'
names['LeftAnkleD'] = 'ValveBiped.Bip01_L_Foot'
names['LegTipEX_R'] = 'ValveBiped.Bip01_R_Toe0'
names['LegTipEX_L'] = 'ValveBiped.Bip01_L_Toe0'
names['RightLegTipEX'] = 'ValveBiped.Bip01_R_Toe0'
names['LeftLegTipEX'] = 'ValveBiped.Bip01_L_Toe0'

#names[''] = 'Helper_Pectoral_R'
#names[''] = 'Helper_Pectoral_L'
#names[''] = 'Helper_Latt_R'
#names[''] = 'Helper_Latt_L'
#names[''] = 'Helper_Trapezius_R'
#names[''] = 'Helper_Trapezius_L'
names['Clavicle_R'] = 'ValveBiped.Bip01_R_Clavicle'
names['Clavicle_L'] = 'ValveBiped.Bip01_L_Clavicle'
names['Right_shoulder'] = 'ValveBiped.Bip01_R_Clavicle'
names['Left_shoulder'] = 'ValveBiped.Bip01_L_Clavicle'
names['Right shoulder'] = 'ValveBiped.Bip01_R_Clavicle'
names['Left shoulder'] = 'ValveBiped.Bip01_L_Clavicle'
names['Rightshoulder'] = 'ValveBiped.Bip01_R_Clavicle'
names['Leftshoulder'] = 'ValveBiped.Bip01_L_Clavicle'
#names[''] = 'Helper_Shoulder_R'
#names[''] = 'Helper_Shoulder_L'
#names[''] = 'Helper_Bicep_R'
#names[''] = 'Helper_Bicep_L'
names['Arm_R'] = 'ValveBiped.Bip01_R_UpperArm'
names['Arm_L'] = 'ValveBiped.Bip01_L_UpperArm'
names['Right_arm'] = 'ValveBiped.Bip01_R_UpperArm'
names['Left_arm'] = 'ValveBiped.Bip01_L_UpperArm'
names['Right arm'] = 'ValveBiped.Bip01_R_UpperArm'
names['Left arm'] = 'ValveBiped.Bip01_L_UpperArm'
names['Rightarm'] = 'ValveBiped.Bip01_R_UpperArm'
names['Leftarm'] = 'ValveBiped.Bip01_L_UpperArm'
names['RightArm'] = 'ValveBiped.Bip01_R_UpperArm'
names['LeftArm'] = 'ValveBiped.Bip01_L_UpperArm'
#names[''] = 'Helper_Elbow_R'
#names[''] = 'Helper_Elbow_L'
names['Elbow_R'] = 'ValveBiped.Bip01_R_Forearm'
names['Elbow_L'] = 'ValveBiped.Bip01_L_Forearm'
names['Right_elbow'] = 'ValveBiped.Bip01_R_Forearm'
names['Left_elbow'] = 'ValveBiped.Bip01_L_Forearm'
names['Right elbow'] = 'ValveBiped.Bip01_R_Forearm'
names['Left elbow'] = 'ValveBiped.Bip01_L_Forearm'
names['Rightelbow'] = 'ValveBiped.Bip01_R_Forearm'
names['Leftelbow'] = 'ValveBiped.Bip01_L_Forearm'
names['RightElbow'] = 'ValveBiped.Bip01_R_Forearm'
names['LeftElbow'] = 'ValveBiped.Bip01_L_Forearm'
#names['HandTwist1_R'] = 'Helper_Ulna_R'
#names['HandTwist1_L'] = 'Helper_Ulna_L'
names['HandTwist2_R'] = 'Helper_Ulna_R'
names['HandTwist2_L'] = 'Helper_Ulna_L'
names['HandTwist3_R'] = 'Helper_Ulna_R'
names['HandTwist3_L'] = 'Helper_Ulna_L'
names['HandTwist_R'] = 'Helper_Wrist_R'
names['HandTwist_L'] = 'Helper_Wrist_L'
names['Wrists_R'] = 'ValveBiped.Bip01_R_Hand'
names['Wrists_L'] = 'ValveBiped.Bip01_L_Hand'
names['Right wrist'] = 'ValveBiped.Bip01_R_Hand'
names['Left wrist'] = 'ValveBiped.Bip01_L_Hand'
names['Rightwrist'] = 'ValveBiped.Bip01_R_Hand'
names['Leftwrist'] = 'ValveBiped.Bip01_L_Hand'
names['RightWrist'] = 'ValveBiped.Bip01_R_Hand'
names['LeftWrist'] = 'ValveBiped.Bip01_L_Hand'
names['Right_wrist'] = 'ValveBiped.Bip01_R_Hand'
names['Left_wrist'] = 'ValveBiped.Bip01_L_Hand'

names['Thumb0_R'] = 'ValveBiped.Bip01_R_Finger0'
names['Thumb0_L'] = 'ValveBiped.Bip01_L_Finger0'
names['Thumb1_R'] = 'ValveBiped.Bip01_R_Finger01'
names['Thumb1_L'] = 'ValveBiped.Bip01_L_Finger01'
names['Thumb2_R'] = 'ValveBiped.Bip01_R_Finger02'
names['Thumb2_L'] = 'ValveBiped.Bip01_L_Finger02'

names['IndexFinger1_R'] = 'ValveBiped.Bip01_R_Finger1'
names['IndexFinger1_L'] = 'ValveBiped.Bip01_L_Finger1'
names['IndexFinger2_R'] = 'ValveBiped.Bip01_R_Finger11'
names['IndexFinger2_L'] = 'ValveBiped.Bip01_L_Finger11'
names['IndexFinger3_R'] = 'ValveBiped.Bip01_R_Finger12'
names['IndexFinger3_L'] = 'ValveBiped.Bip01_L_Finger12'

names['MiddleFinger1_R'] = 'ValveBiped.Bip01_R_Finger2'
names['MiddleFinger1_L'] = 'ValveBiped.Bip01_L_Finger2'
names['MiddleFinger2_R'] = 'ValveBiped.Bip01_R_Finger21'
names['MiddleFinger2_L'] = 'ValveBiped.Bip01_L_Finger21'
names['MiddleFinger3_R'] = 'ValveBiped.Bip01_R_Finger22'
names['MiddleFinger3_L'] = 'ValveBiped.Bip01_L_Finger22'

names['RingFinger1_R'] = 'ValveBiped.Bip01_R_Finger3'
names['RingFinger1_L'] = 'ValveBiped.Bip01_L_Finger3'
names['RingFinger2_R'] = 'ValveBiped.Bip01_R_Finger31'
names['RingFinger2_L'] = 'ValveBiped.Bip01_L_Finger31'
names['RingFinger3_R'] = 'ValveBiped.Bip01_R_Finger32'
names['RingFinger3_L'] = 'ValveBiped.Bip01_L_Finger32'

names['LittleFinger1_R'] = 'ValveBiped.Bip01_R_Finger4'
names['LittleFinger1_L'] = 'ValveBiped.Bip01_L_Finger4'
names['LittleFinger2_R'] = 'ValveBiped.Bip01_R_Finger41'
names['LittleFinger2_L'] = 'ValveBiped.Bip01_L_Finger41'
names['LittleFinger3_R'] = 'ValveBiped.Bip01_R_Finger42'
names['LittleFinger3_L'] = 'ValveBiped.Bip01_L_Finger42'

names['RightThumb0'] = 'ValveBiped.Bip01_R_Finger0'
names['LeftThumb0'] = 'ValveBiped.Bip01_L_Finger0'
names['RightThumb1'] = 'ValveBiped.Bip01_R_Finger01'
names['LeftThumb1'] = 'ValveBiped.Bip01_L_Finger01'
names['RightThumb2'] = 'ValveBiped.Bip01_R_Finger02'
names['LeftThumb2'] = 'ValveBiped.Bip01_L_Finger02'

names['RightIndexFinger1'] = 'ValveBiped.Bip01_R_Finger1'
names['LeftIndexFinger1'] = 'ValveBiped.Bip01_L_Finger1'
names['RightIndexFinger2'] = 'ValveBiped.Bip01_R_Finger11'
names['LeftIndexFinger2'] = 'ValveBiped.Bip01_L_Finger11'
names['RightIndexFinger3'] = 'ValveBiped.Bip01_R_Finger12'
names['LeftIndexFinger3'] = 'ValveBiped.Bip01_L_Finger12'

names['RightMiddleFinger1'] = 'ValveBiped.Bip01_R_Finger2'
names['LeftMiddleFinger1'] = 'ValveBiped.Bip01_L_Finger2'
names['RightMiddleFinger2'] = 'ValveBiped.Bip01_R_Finger21'
names['LeftMiddleFinger2'] = 'ValveBiped.Bip01_L_Finger21'
names['RightMiddleFinger3'] = 'ValveBiped.Bip01_R_Finger22'
names['LeftMiddleFinger3'] = 'ValveBiped.Bip01_L_Finger22'

names['RightRingFinger1'] = 'ValveBiped.Bip01_R_Finger3'
names['LeftRingFinger1'] = 'ValveBiped.Bip01_L_Finger3'
names['RightRingFinger2'] = 'ValveBiped.Bip01_R_Finger31'
names['LeftRingFinger2'] = 'ValveBiped.Bip01_L_Finger31'
names['RightRingFinger3'] = 'ValveBiped.Bip01_R_Finger32'
names['LeftRingFinger3'] = 'ValveBiped.Bip01_L_Finger32'

names['RightLittleFinger1'] = 'ValveBiped.Bip01_R_Finger4'
names['LeftLittleFinger1'] = 'ValveBiped.Bip01_L_Finger4'
names['RightLittleFinger2'] = 'ValveBiped.Bip01_R_Finger41'
names['LeftLittleFinger2'] = 'ValveBiped.Bip01_L_Finger41'
names['RightLittleFinger3'] = 'ValveBiped.Bip01_R_Finger42'
names['LeftLittleFinger3'] = 'ValveBiped.Bip01_L_Finger42'

names['weapon_bone_L'] = 'weapon_bone_L'
names['weapon_bone'] = 'weapon_bone_R'

#used by witch particle
names['Bone_Eye_L_End'] = 'leye'
names['Bone_Eye_R_End'] = 'reye'

