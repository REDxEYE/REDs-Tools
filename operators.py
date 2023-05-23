import bpy
import math
from mathutils import Vector, Euler, Matrix

from bpy.props import *

#from .bone_table import bone_table_valvebiped, bone_table_bip

from .rename_dicts.bio3_to_tf2 import names as bio3_to_tf2
from .rename_dicts.valvebiped_to_blender import names as valvebiped_to_blender
from .rename_dicts.tf2_to_blender import names as tf2_to_blender
from .rename_dicts.rxd_blender import names as rxd_to_blender
from .rename_dicts.rigfy_to_blender import names as rigfy_to_blender
from .rename_dicts.mmd_to_valvebiped import names as mmd_to_valvebiped
from .rename_dicts.kofas_blender import names as kofas_to_blender
from .rename_dicts.fortnite_to_blender import names as fortnite_to_blender
from .rename_dicts.cybersleuth_to_blender import names as cybersleuth_to_blender
from .rename_dicts.blender_to_valvebiped import names as blender_to_valvebiped


def enable_if(context, is_mode):
    '''return True if active object is in is_mode'''
    return context.active_object and context.active_object.type == is_mode


def get_bonechain(val):
    bone_chains = {
        'LARM': ['shoulder.l', 'upperarm.l', 'forearm.l', 'hand.l'],
        'RARM': ['shoulder.r', 'upperarm.r', 'forearm.r', 'hand.r'],
        'LLEG': ['hip.l', 'knee.l', 'foot.l', 'toe.l'],
        'RLEG': ['hip.r', 'knee.r', 'foot.r', 'toe.r'],
        'LTUMB': ['fing.Thumb0.l', 'fing.Thumb1.l', 'fing.Thumb2.l'],
        'RTUMB': ['fing.Thumb0.r', 'fing.Thumb1.r', 'fing.Thumb2.r'],
        'LINDX': ['fing.Index0.l', 'fing.Index1.l', 'fing.Index2.l'],
        'RINDX': ['fing.Index0.r', 'fing.Index1.r', 'fing.Index2.r'],
        'LMIDL': ['fing.Middle0.l', 'fing.Middle1.l', 'fing.Middle2.l'],
        'RMIDL': ['fing.Middle0.r', 'fing.Middle1.r', 'fing.Middle2.r'],
        'LRNG': ['fing.Ring0.l', 'fing.Ring1.l', 'fing.Ring2.l'],
        'RRNG': ['fing.Ring0.r', 'fing.Ring1.r', 'fing.Ring2.r'],
        'LPNK': ['fing.Pinky0.l', 'fing.Pinky1.l', 'fing.Pinky2.l'],
        'RPNK': ['fing.Pinky0.r', 'fing.Pinky1.r', 'fing.Pinky2.r'],

    }
    return bone_chains[val]


def find_line_of_sight(start, end):
    chain = []
    bone = end
    chain.append(end)
    for _ in range(3):
        if bone is None:
            return find_line_of_sight(end, start)
        bone = bone.parent
        chain.append(bone)
        if bone == start:
            break
    if chain[-1] != start:
        print('SOMETHING WENT WRONG!', chain)
    return chain


def close(a, b):
    '''return abs(a - b) < 0.1'''
    return abs(a - b) < 0.1


def find_mirror_bone(ob, bone):
    '''We don't care for names here, return bone object which have a X-Mirror aesthetic'''
    for o_bone in ob.pose.bones:
        if bone != o_bone and \
                close(o_bone.head.x, (-1 * bone.head.x)) and \
                close(o_bone.head.y, bone.head.y) and \
                close(o_bone.head.z, bone.head.z):
            return o_bone


def mirror_name(name):
    '''return mirror name postfix.
    Note: is this deprecated?'''
    if name[-1].upper() == 'L':
        return name[:-1] + 'R'
    if name[-1].upper() == 'R':
        return name[:-1] + 'L'


def bone_list_switch(case):
    '''Select and return the bone dictionary from above imports

    obs: I do know Python 3.11 support case switch statement, however this addon target support to 2.8x'''
    if case == "blender_valve":
        return blender_to_valvebiped
    if case == "valve_blender":
        return valvebiped_to_blender
    if case == "dscs_to_blender":
        return cybersleuth_to_blender
    if case == "rxd_blender":
        return rxd_to_blender
    if case == "rigfy_blender":
        return rigfy_to_blender
    if case == "mmd_valvebiped":
        return mmd_to_valvebiped
    if case == "kofas_blender":
        return kofas_to_blender
    if case == "fortnite_blender":
        return fortnite_to_blender
    if case == "tf2_blender":
        return tf2_to_blender
    if case == "bio3_tf2":
        return bio3_to_tf2
    print("[ERROR]: The list used by bone_list_switch() doesn't exist")


def is_mode(a, b):
    '''if object ins not on mode {1}, set the object into {2}'''
    if bpy.context.mode != a : bpy.ops.object.mode_set(mode=b)


def set_mode(vm):
    '''If mode_set not in vm, set mode_set vm'''
    # cveats for ARMATURE
    if vm == 'EDIT_ARMATURE':
        bpy.ops.object.mode_set(mode='EDIT')
    else:
        bpy.ops.object.mode_set(mode=vm)


def set_active_object(object_name):
    '''set object_name as active object'''
    bpy.context.view_layer.objects.active = bpy.data.objects[object_name]
    bpy.data.objects[object_name].select_set(state=True)


def get_edit_bone(name):
    '''return bone if editable bone name exists for active object'''
    return bpy.context.object.data.edit_bones.get(name)


def get_pose_bone(name):
    '''return bone if pose bone name exists for active object'''
    return bpy.context.active_object.pose.bones.get(name)


def get_object(name):
    '''return object if name exists for active object'''
    return bpy.data.objects.get(name)
        

def select_bones_if_nothing():
    '''Select All bones in case theres no bones selected for active object'''
    if bpy.context.selected_editable_bones == []:
        bpy.ops.armature.select_all(action='SELECT')


def mat3_to_vec_roll(mat):
    vec = mat.col[1]
    vecmat = vec_roll_to_mat3(mat.col[1], 0)
    vecmatinv = vecmat.inverted()
    rollmat = vecmatinv @ mat
    roll = math.atan2(rollmat[0][2], rollmat[2][2])
    return vec, roll


def vec_roll_to_mat3(vec, roll):
    target = Vector((0, 0.1, 0))
    nor = vec.normalized()
    axis = target.cross(nor)
    if axis.dot(axis) > 0.0000000001: # this seems to be the problem euler some bones, no idea how to fix
        axis.normalize()
        theta = target.angle(nor)
        bMatrix = Matrix.Rotation(theta, 3, axis)
    else:
        updown = 1 if target.dot(nor) > 0 else -1
        bMatrix = Matrix.Scale(updown, 3)               
        bMatrix[2][2] = 1.0

    rMatrix = Matrix.Rotation(roll, 3, nor)
    mat = rMatrix @ bMatrix
    return mat


def hierarchy(child, parent):
    '''Mimics $hierarchy QC Command from Source Engine.\n
    This makes {1} be child of {2}'''
    is_mode('EDIT_ARMATURE', 'EDIT')
    bone1 = get_edit_bone(child)
    bone2 = get_edit_bone(parent)
    if (bone1) and (bone2):
        bone1.parent = bone2


def helper(helper, parent):
    ''''This try make hierarchy using some obvious format styles'''
    h = 'Helper_'
    v = 'ValveBiped.Bip01_'
    # Helpers format I often use
    hierarchy(h+helper+'_L', v+'L_'+parent)
    hierarchy(h+helper+'_R', v+'R_'+parent)
    # Helpers which I often don't use
    hierarchy(h+'L_'+helper, v+'L_'+parent)
    hierarchy(h+'R_'+helper, v+'R_'+parent)
    # ValveBiped-like format
    hierarchy(v+'L_'+helper, v+'L_'+parent)
    hierarchy(v+'R_'+helper, v+'R_'+parent)


def helperm(helper, parent):
    ''''This try make hierarchy using some obvious format styles'''
    h = 'Helper_'
    v = 'ValveBiped.Bip01_'
    # Helpers format I often use
    hierarchy(h+helper+'_L', v+parent)
    hierarchy(h+helper+'_R', v+parent)
    # Helpers which I often don't use
    hierarchy(h+'L_'+helper, v+parent)
    hierarchy(h+'R_'+helper, v+parent)
    # ValveBiped-like format
    hierarchy(v+'L_'+helper, v+parent)
    hierarchy(v+'R_'+helper, v+parent)


def toggle_material_nodes(bool=False):
    for EachMaterial in bpy.data.materials:
       EachMaterial.use_nodes = bool


class VALVE_OT_CleanBonesShape(bpy.types.Operator):
    """Remove custom shapes for selected bones"""
    bl_idname = "valve.bones_shape_clear"
    bl_label = "Remove custom shapes"
    bl_description = "Remove custom shapes for selected bones"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')
        
    def execute(self, context):
        ob = context.active_object
        if ob.type == "ARMATURE":
            for bone in ob.pose.bones:
                bone.custom_shape = None
        else:
            self.report({"ERROR"},
                        "What? What am I supposed to do with this {}? I need armature!!!! GIVE ME MY ARMATURE!"
                        .format(ob.type.lower()))
        return {'FINISHED'}


class VALVE_OT_RenameBonesTo(bpy.types.Operator):
    """Rename Bones to selected BoneList dictionary"""
    bl_idname = "valve.rename_bones_dict"
    bl_label = "Rename bones"
    bl_description = "Rename bones from the selected armature using above \"Bone list\" dictionary"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')

    def execute(self, context):
        ob = context.active_object
        if not ob:
            self.report({"ERROR"}, "Select something!")
            return {'FINISHED'}
        if ob.type == "ARMATURE":
            bones = ob.data.bones

            names = bone_list_switch(bpy.context.scene.BoneList)

            if (bones):
                for bone in bones:
                    newName = names.get(bone.name)
                    if (newName):
                        bone.name = newName

        else:
            self.report({"ERROR"},
                        "What is this? {} is not armature! I need armature!".format(ob.type.lower().title()))
        return {'FINISHED'}


class ARMATURE_OT_LockBoneLocation(bpy.types.Operator):
    """Lock All ValveBiped bones position.
    Useful for retarget poses"""
    bl_idname = "armature.bone_location_lock"
    bl_label = "Lock Loc"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')

    def execute(self, context):
        prefix = "ValveBiped"
        armature = context.active_object.pose.bones

        for bone in armature:
            if bone.name.lower().startswith(prefix.lower()):
                has_constraint = False
                for const in bone.constraints:
                    if const.type == 'LIMIT_LOCATION' and const.name == "Lock Location":
                        has_constraint = True
                        break
                if not has_constraint:
                    const = bone.constraints.new(type='LIMIT_LOCATION')
                    const.name = "Lock Location"
                    const.owner_space = 'LOCAL'
                    const.use_transform_limit = True
                    const.use_min_x = True
                    const.use_max_x = True
                    const.use_min_y = True
                    const.use_max_y = True
                    const.use_min_z = True
                    const.use_max_z = True
        return {'FINISHED'}


class ARMATURE_OT_SetBoneViewMode(bpy.types.Operator):
    """For all selected bones, define a specific viewport display"""
    bl_idname = "valve.bone_viewmode"
    bl_label = "Setup Bone Viewmode"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')

    def execute(self, context):
        is_mode('EDIT_ARMATURE', 'EDIT')

        ob = context.active_object

        select_bones_if_nothing

        for bone in context.selected_editable_bones:
            bone.envelope_distance = 6.0
            bone.length = 3.0

        set_mode('POSE')

        for bone in context.selected_pose_bones_from_active_object:
            bone.custom_shape = get_object('smd_bone_vis')
            bone.use_custom_shape_bone_size = False
            for n in range(3):
                bone.custom_shape_scale_xyz[n] = 0.2

        set_mode('OBJECT')

        name = ob.name
        bpy.data.objects[name].display_type = 'WIRE'
        bpy.data.objects[name].show_in_front = True
        a = ob.data
        a.display_type = 'STICK'
        a.show_axes = True
        a.show_bone_custom_shapes = True
        a.show_group_colors = True

        return {'FINISHED'}


class ARMATURE_OT_SetBoneHierarchy(bpy.types.Operator):
    """Enforce ValveBiped hierarchy"""
    bl_idname = "valve.bone_hierarchy"
    bl_label = "Valve Hierarchy"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return enable_if(context, 'ARMATURE')

    def execute(self, context):
        vm = context.mode
        is_mode('EDIT_ARMATURE', 'EDIT')

        # TODO: adicionar um seletor.
        # ValveBiped Hierarchy
        v = 'ValveBiped.Bip01_'
        hierarchy(v+'Pelvis', "")
        hierarchy(v+'Spine', v+'Pelvis')
        hierarchy(v+'Spine1', v+'Spine')
        hierarchy(v+'Spine2', v+'Spine1')
        hierarchy(v+'Spine4', v+'Spine2')
        hierarchy(v+'Neck1', v+'Spine4')
        hierarchy(v+'Head1', v+'Neck1')
        hierarchy(v+'L_Clavicle', v+'Spine4')
        hierarchy(v+'L_UpperArm', v+'L_Clavicle')
        hierarchy(v+'L_Forearm', v+'L_UpperArm')
        hierarchy(v+'L_Hand', v+'L_Forearm')

        hierarchy(v+'L_Finger0', v+'L_Hand')
        hierarchy(v+'L_Finger01', v+'L_Finger0')
        hierarchy(v+'L_Finger02', v+'L_Finger01')
        hierarchy(v+'L_Finger1', v+'L_Hand')
        hierarchy(v+'L_Finger11', v+'L_Finger1')
        hierarchy(v+'L_Finger12', v+'L_Finger11')
        hierarchy(v+'L_Finger2', v+'L_Hand')
        hierarchy(v+'L_Finger21', v+'L_Finger2')
        hierarchy(v+'L_Finger22', v+'L_Finger21')
        hierarchy(v+'L_Finger3', v+'L_Hand')
        hierarchy(v+'L_Finger31', v+'L_Finger3')
        hierarchy(v+'L_Finger32', v+'L_Finger31')
        hierarchy(v+'L_Finger4', v+'L_Hand')
        hierarchy(v+'L_Finger41', v+'L_Finger4')
        hierarchy(v+'L_Finger42', v+'L_Finger41')

        hierarchy(v+'R_Clavicle', v+'Spine4')
        hierarchy(v+'R_UpperArm', v+'R_Clavicle')
        hierarchy(v+'R_Forearm', v+'R_UpperArm')
        hierarchy(v+'R_Hand', v+'R_Forearm')

        hierarchy(v+'R_Finger0', v+'R_Hand')
        hierarchy(v+'R_Finger01', v+'R_Finger0')
        hierarchy(v+'R_Finger02', v+'R_Finger01')
        hierarchy(v+'R_Finger1', v+'R_Hand')
        hierarchy(v+'R_Finger11', v+'R_Finger1')
        hierarchy(v+'R_Finger12', v+'R_Finger11')
        hierarchy(v+'R_Finger2', v+'R_Hand')
        hierarchy(v+'R_Finger21', v+'R_Finger2')
        hierarchy(v+'R_Finger22', v+'R_Finger21')
        hierarchy(v+'R_Finger3', v+'R_Hand')
        hierarchy(v+'R_Finger31', v+'R_Finger3')
        hierarchy(v+'R_Finger32', v+'R_Finger31')
        hierarchy(v+'R_Finger4', v+'R_Hand')
        hierarchy(v+'R_Finger41', v+'R_Finger4')
        hierarchy(v+'R_Finger42', v+'R_Finger41')

        hierarchy(v+'L_Thigh', v+'Pelvis')
        hierarchy(v+'L_Calf', v+'L_Thigh')
        hierarchy(v+'L_Foot', v+'L_Calf')
        hierarchy(v+'L_Toe', v+'L_Foot')
        hierarchy(v+'L_Toe0', v+'L_Foot')
        hierarchy(v+'L_Toe1', v+'L_Foot')
        hierarchy(v+'L_Toe2', v+'L_Foot')
        hierarchy(v+'L_Toe3', v+'L_Foot')
        hierarchy(v+'L_Toe4', v+'L_Foot')
        hierarchy(v+'R_Thigh', v+'Pelvis')
        hierarchy(v+'R_Calf', v+'R_Thigh')
        hierarchy(v+'R_Foot', v+'R_Calf')
        hierarchy(v+'R_Toe', v+'R_Foot')
        hierarchy(v+'R_Toe0', v+'R_Foot')
        hierarchy(v+'R_Toe1', v+'R_Foot')
        hierarchy(v+'R_Toe2', v+'R_Foot')
        hierarchy(v+'R_Toe3', v+'R_Foot')
        hierarchy(v+'R_Toe4', v+'R_Foot')

        # usual Helpers / Procedural hierarchy
        hierarchy('Helper_Neck', 'ValveBiped.Bip01_Neck1')
        hierarchy('Helper_Head', 'ValveBiped.Bip01_Head1')
        helperm('Latt', 'Spine2')
        helper('Trapezius', 'Clavicle')
        helper('Armor', 'UpperArm')
        helper('Shoulder', 'UpperArm')
        helper('UpperArm_twist', 'UpperArm')
        helper('Bicep', 'UpperArm')
        helper('Elbow', 'UpperArm')
        helper('Ulna', 'Forearm')
        helper('Wrist', 'Forearm')
        helper('Thumb_root', 'Hand')
        helper('Hip', 'Thigh')
        helper('Hips', 'Thigh')
        helper('Sartorius', 'Thigh')
        helper('Quadricep', 'Thigh')
        helper('Quad', 'Thigh')
        helper('Knee', 'Thigh')
        helper('Shin', 'Calf')
        helper('Soleous', 'Calf')
        helper('Ankle', 'Calf')
        helper('Thumb', 'Foot')
        helper('Pinky', 'Foot')
        helper('Toe', 'Foot')

        set_mode(vm)

        return {'FINISHED'}


class VALVE_OT_ConnectBones(bpy.types.Operator):
    """Conect all detached bones to it child following the constraint"""
    bl_idname = "valve.armature_connect"
    bl_label = "Connect bones"

    @classmethod
    def poll(self, context):
        return True if context.active_object is not None and (context.active_object.type == 'ARMATURE') else False


    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        for bone_ in context.selected_editable_bones:

            if bone_.parent:
                parent = bone_.parent
                if len(parent.children) > 1:
                    bone_.use_connect = False
                    parent.tail = sum([ch.head for ch in parent.children], Vector()) / len(parent.children)
                else:
                    parent.tail = bone_.head
                    bone_.use_connect = True
                    if bone_.children == 0:
                        par = bone_.parent
                        if par.children > 1:
                            pass
                        bone_.tail = bone_.head + (par.tail - par.head)
                    if not bone_.parent and bone_.children > 1:
                        bone_.tail = (bone_.head + bone_.tail) * 2
                if bone_.head == parent.head:
                    print(bone_.name)
                    bone_.tail = parent.tail
                elif not bone_.children:
                    vec = bone_.parent.head - bone_.head
                    bone_.tail = bone_.head - vec / 2

        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z')
        bpy.ops.object.mode_set(mode='POSE')
        return {'FINISHED'}


class VALVE_OT_MergeBoneWeights(bpy.types.Operator):
    """this works?
    seems it try to join weights from all selected bones to active bone"""
    bl_idname = "valve.armature_merge"
    bl_label = "Merge bone weights"

    @classmethod
    def poll(self, context):
        if (context.active_object):
            if context.active_object.type == 'ARMATURE':
                if context.active_object.mode == 'POSE':
                    return True
        return False

    def execute(self, context):
        this = context.active_pose_bone
        others = context.selected_pose_bones[1:]
        arm = this.id_data
        for other in others:
            for child in arm.children:
                # print(child)
                if child.type == 'MESH':
                    modifier = child.modifiers.new(type='VERTEX_WEIGHT_MIX', name='MERGE_{}_TO_{}'.format(other.name,this.name))
                    # print(modifier, this, other)
                    # print(child, child.type, modifier, this, other)
                    modifier.vertex_group_a = this.name
                    modifier.vertex_group_b = other.name
                    modifier.mix_mode = 'ADD'
                    modifier.mix_set = 'ALL'
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

        return {'FINISHED'}


''' NOTE: super seeded by bpy.ops.pose.constraints_clear()
class VALVE_OT_CleanBonesConstraints(bpy.types.Operator):
    bl_idname = "valve.cleanbonesconstraints"
    bl_label = "Remove constraints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ob = context.active_object
        if ob.type == "ARMATURE":
            for bone in ob.pose.bones:
                for c in bone.constraints:
                    bone.constraints.remove(c)
        else:
            self.report({"ERROR"},
                        "What? What am I supposed to do with this {}? I need armature!!!! GIVE ME MY ARMATURE!"
                        .format(ob.type.lower()))
        return {'FINISHED'}


class VALVE_OT_RenameBoneChains(bpy.types.Operator):
    bl_idname = "valve.renamebonechain"
    bl_label = "Rename chain"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ob = context.active_object
        if not ob:
            self.report({"ERROR"}, "Select something!")
            return {'FINISHED'}
        if ob.type == "ARMATURE":
            name_dict = bone_table_valvebiped if context.scene.NameFormat == 1 else bone_table_bip
            bone_chain = get_bonechain(context.scene.BoneChains)
            end = context.active_pose_bone
            bones = context.selected_pose_bones
            bones.remove(end)
            bones.append(end)
            current_chain = context.scene.BoneChains
            if not bones:
                self.report({"ERROR"}, "Have you read \"How to use?\"? I think No.")
                return {'FINISHED'}
            bones = find_line_of_sight(bones[0], bones[1])
            print('CHAIN', bones)
            bone_names = bone_chain
            if current_chain in ['LARM', 'RARM', 'LLEG', 'RLEG'] and len(bones) == 3:
                bone_names = bone_names[:-1]
            if len(bones) == 2:
                bone_names = bone_names
                for n, bone in enumerate(bones[::-1]):
                    # if find_mirror_bone(ob, bone):
                    #     find_mirror_bone(ob, bone).name = mirror_name(name_dict[bone_names[n]])
                    bone.name = name_dict[bone_names[n]]
            else:
                bone_names = bone_names[::-1]
                for n, bone in enumerate(bones):
                    # if find_mirror_bone(ob, bone):
                    #     find_mirror_bone(ob, bone).name = mirror_name(name_dict[bone_names[n]])
                    bone.name = name_dict[bone_names[n]]
                # start_bone = context.selected
        else:
            self.report({"ERROR"},
                        "What is this? {} is not armature! I need armature!".format(ob.type.lower().title()))
        return {'FINISHED'}


# noinspection PyPep8Naming,PyMethodMayBeStatic
class VALVE_OT_RenameChainPopup(bpy.types.Operator):
    """Help popup"""
    bl_idname = "valve.renamechainpopup"
    bl_label = "How to use!"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = int(400 * bpy.context.preferences.system.pixel_size)
        return context.window_manager.invoke_props_dialog(self, width=width)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="How to use!")
        col = box.column(align=True)
        col.label(text="Select start bone, ex:collar bone or upperarm bone")
        col.separator()
        col.label(text="Then select end bone, ex:foot bone or toe bone")
        col.label(text="After all this click \"Rename limb\"")

    def execute(self, context):
        return {'FINISHED'}


class BONES_TP_CompareArmatures(bpy.types.Operator):
    """Compared 2 armatures"""
    bl_idname = "valve.comparearmatures"
    bl_label = "Compare 2 armatures"
    bl_options = {'REGISTER', 'UNDO'}

    def compare(self, armatures):
        missing = []
        parent_diff = []
        arm1 = armatures[0]
        arm2 = armatures[1]
        bones1 = arm1.data.bones
        bones2 = arm2.data.bones

        for bone1 in bones1:
            bone2 = bones2.get(bone1.name, None)
            if bone2 is None:
                missing.append(bone1.name)
                continue
            if bone1.parent is not None and bone2.parent is not None:
                if bone1.parent.name != bone2.parent.name:
                    parent_diff.append(bone1.name)
        return missing, parent_diff

    def execute(self, context):
        from ctypes import windll
        k32 = windll.LoadLibrary('kernel32.dll')
        setConsoleModeProc = k32.SetConsoleMode
        setConsoleModeProc(k32.GetStdHandle(-11), 0x0001 | 0x0002 | 0x0004)
        armatures = bpy.context.selected_objects
        missing, parent_diff = self.compare(armatures)
        print('\033[94mMissing bones on {}\033[0m'.format(armatures[0].name))
        for mis in missing:
            print('\033[91m{}\033[0m'.format(mis))
        missing, parent_diff = self.compare(armatures[::-1])
        print('\033[94mMissing bones on {}\033[0m'.format(armatures[1].name))
        for mis in missing:
            print('\033[91m{}\033[0m'.format(mis))
        print('\033[94mDifferent parents {}\033[0m'.format(armatures[1].name))
        for mis in parent_diff:
            print('\033[91m{}\033[0m'.format(mis))

        return {'FINISHED'}
'''