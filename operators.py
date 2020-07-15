import bpy

from bpy.props import *

from .bone_table import bone_table_valvebiped, bone_table_bip


def track_l_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_L']
    bpy.context.scene.LeftEye = obj.location


def track_r_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_R']
    bpy.context.scene.RightEye = obj.location


# noinspection PyPep8Naming,PyMethodMayBeStatic
class EYES_OT_CreateEyeDummies(bpy.types.Operator):
    bl_idname = "create.eyedummy"
    bl_label = "Create eye dummies"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass
        if not (
            bpy.data.objects.get('VALVE_EYEDUMMY_L', None)
            and bpy.data.objects.get('VALVE_EYEDUMMY_R', None)
        ):
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5)
            eye_L = context.active_object
            eye_L.name = 'VALVE_EYEDUMMY_L'
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5)
            eye_R = context.active_object
            eye_R.name = 'VALVE_EYEDUMMY_R'
            bpy.app.handlers.depsgraph_update_post.append(track_l_eye)
            bpy.app.handlers.depsgraph_update_post.append(track_r_eye)
            bpy.ops.qceyes.popup('EXEC_DEFAULT')
        return {'FINISHED'}


attachment_string = '$Attachment "{name}" "{p_bone}" {x} {y} {z} absolute\n'
eyeball_string = 'eyeball {eyeball_side} "{p_bone}" {x} {y} {z} "{mat_name}" 3 {angle} "iris_unused" {size}\n'
flexcont_string = 'flexcontroller eyes range -{angle1} {angle2} {fc_type}\n'


# noinspection PyPep8Naming
class BONES_OT_CleanBones(bpy.types.Operator):
    bl_idname = "valve.cleanbones"
    bl_label = "Remove custom shapes"
    bl_options = {'REGISTER', 'UNDO'}

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


# noinspection PyPep8Naming
class BONES_OT_CleanBonesConstraints(bpy.types.Operator):
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


# noinspection PyPep8Naming
class BONES_OT_QCEyesQCGenerator(bpy.types.Operator):
    bl_idname = "qceyes.generate_qc"
    bl_label = "Generate QC string"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        eye_l = bpy.data.objects.get('VALVE_EYEDUMMY_L', None)
        eye_r = bpy.data.objects.get('VALVE_EYEDUMMY_R', None)
        p_bone = bpy.data.objects[str(bpy.context.scene.Armature)].data.bones[str(bpy.context.scene.HeadBone)]
        if eye_l and eye_r:
            if not bpy.data.texts.get("qc_eyes.qc", None):
                qc_string = bpy.data.texts.new('qc_eyes.qc')
            else:
                qc_string = bpy.data.texts['qc_eyes.qc']
            qc_string.write(attachment_string.format(name="eyes", p_bone=p_bone.name,
                                                     x=abs(eye_r.location.x) - abs(eye_l.location.x),
                                                     y=avg(eye_l.location.y, eye_r.location.y),
                                                     z=avg(eye_l.location.z, eye_r.location.z)))
            qc_string.write(attachment_string.format(name="righteye", p_bone=p_bone.name,
                                                     x=eye_r.location.x,
                                                     y=eye_r.location.y,
                                                     z=eye_r.location.z))
            qc_string.write(attachment_string.format(name="lefteye", p_bone=p_bone.name,
                                                     x=eye_l.location.x,
                                                     y=eye_l.location.y,
                                                     z=eye_l.location.z))
            qc_string.write('\n')

            qc_string.write(eyeball_string.format(eyeball_side="righteye", p_bone=p_bone.name,
                                                  x=eye_l.location.x,
                                                  y=eye_l.location.y,
                                                  z=eye_l.location.z,
                                                  mat_name=bpy.context.scene.RightEyeMat,
                                                  angle=bpy.context.scene.AngDev,
                                                  size=eye_r.scale.x))
            qc_string.write(eyeball_string.format(eyeball_side="lefteye", p_bone=p_bone.name,
                                                  x=eye_l.location.x,
                                                  y=eye_l.location.y,
                                                  z=eye_l.location.z,
                                                  mat_name=bpy.context.scene.LeftEyeMat,
                                                  angle=-bpy.context.scene.AngDev,
                                                  size=eye_r.scale.x))
            qc_string.write('\n')

            qc_string.write(flexcont_string.format(angle1=bpy.context.scene.EyesUp, angle2=bpy.context.scene.EyesDown,
                                                   fc_type='eyes_updown'))
            qc_string.write(
                flexcont_string.format(angle1=bpy.context.scene.EyesRight, angle2=bpy.context.scene.EyesLeft,
                                       fc_type='eyes_rightleft'))

        else:
            self.report({"ERROR"},
                        "Can't find eye dummies, did ya create 'em?")
        return {'FINISHED'}


def avg(*args):
    return sum(args) / len(args)


# noinspection PyPep8Naming
class EYES_OT_QCEyesPopup(bpy.types.Operator):
    """Help popup"""
    bl_idname = "qceyes.popup"
    bl_label = "QC eyes how to use!"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = 400 * bpy.context.preferences.system.pixel_size
        return context.window_manager.invoke_props_dialog(self, width=width)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="How to use!")
        col = box.column(align=True)
        col.label("Place both dummies where eyes supposed to be")
        col.separator()
        col.label("Apply eyes materials to them")
        col.label("After all this trash click \"Generate QC\"")

    def execute(self, context):
        return {'FINISHED'}


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
    return abs(a - b) < 0.1


def find_mirror_bone(ob, bone):
    for o_bone in ob.pose.bones:
        if bone != o_bone and \
                close(o_bone.head.x, (-1 * bone.head.x)) and \
                close(o_bone.head.y, bone.head.y) and \
                close(o_bone.head.z, bone.head.z):
            return o_bone


def mirror_name(name):
    if name[-1].upper() == 'L':
        return name[:-1] + 'R'
    if name[-1].upper() == 'R':
        return name[:-1] + 'L'


# noinspection PyPep8Naming
class BONES_OT_RenameBoneChains(bpy.types.Operator):
    bl_idname = "valve.renamechain"
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
class BONES_OT_RenameChainPopup(bpy.types.Operator):
    """Help popup"""
    bl_idname = "valve.renamechainpopup"
    bl_label = "How to use rename limb !"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = 400 * bpy.context.preferences.system.pixel_size
        return context.window_manager.invoke_props_dialog(self, width=width)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="How to use!")
        col = box.column(align=True)
        col.label("Select start bone, ex:collar bone or upperarm bone")
        col.separator()
        col.label("Then select end bone, ex:foot bone or toe bone")
        col.label("After all this click \"Rename limb\"")

    def execute(self, context):
        return {'FINISHED'}


# noinspection PyPep8Naming
class BONES_TP_CompareArmatures(bpy.types.Operator):
    """Compared 2 armatures"""
    bl_idname = "valve.compare_armatures"
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
