import bpy

from bpy.props import *

from .bone_table import bone_table_valvebiped, bone_table_bip


class ValvePanel(bpy.types.Panel):
    bl_idname = 'valve.panel'
    bl_label = 'Source engine tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Valve'

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        row = layout.row()
        row.label("Target armature")
        row.prop_search(scn, "Armature", scn, "objects", text='')

        layout.separator()
        layout.label("QC eyes")
        box = layout.box()
        column = box.column(align=True)
        column.operator("qceyes.popup")
        column.separator()
        column.operator("create.eyedummy")
        column.operator("qceyes.generate_qc")
        column.separator()
        column = box.column()
        column.prop(scn, 'LeftEye')
        column.prop(scn, 'RightEye')
        column.prop_search(scn, 'LeftEyeMat', bpy.data, 'materials')
        column.prop_search(scn, 'RightEyeMat', bpy.data, 'materials')
        row = column.row()
        row.prop(scn, 'EyesUp')
        row.prop(scn, 'EyesDown')
        row = column.row()
        row.prop(scn, 'EyesLeft')
        row.prop(scn, 'EyesRight')
        column.prop(scn, 'AngDev')
        if scn.Armature and bpy.data.objects[scn.Armature].type == "ARMATURE":
            row = column.row()
            row.label("Head Bone")
            row.prop_search(scn, "HeadBone", bpy.data.objects[scn.Armature].data, "bones", text="")

        layout.separator()
        layout.label("Armature tools")
        layout.label("Work with active armature")
        box = layout.box()
        box.operator("valve.cleanbones")
        box.operator("valve.cleanbonesconstraints")
        box.operator("rename.biped")
        box.operator("rename.bip")
        column = box.column()
        column.prop(scn, 'NameTemplate')
        column.operator('rename.chain')
        box.operator('armature.connect')

        layout.separator()
        layout.label("Rename tools")
        box = layout.box()
        box.operator("valve.renamechainpopup")
        box.separator()
        box.label('Choose name format')
        box.prop(scn, 'NameFormat')
        box.separator()
        box.prop(scn, 'BoneChains')
        box.operator('valve.renamechain')


def track_l_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_L']
    bpy.context.scene.LeftEye = obj.location


def track_r_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_R']
    bpy.context.scene.RightEye = obj.location


class CreateEyeDummys(bpy.types.Operator):
    bl_idname = "create.eyedummy"
    bl_label = "Create eye dummies"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass
        if not bpy.data.objects.get('VALVE_EYEDUMMY_L', None) or not bpy.data.objects.get('VALVE_EYEDUMMY_R', None):
            bpy.ops.mesh.primitive_uv_sphere_add(size=0.5)
            eye_L = context.active_object
            eye_L.name = 'VALVE_EYEDUMMY_L'
            bpy.ops.mesh.primitive_uv_sphere_add(size=0.5)
            eye_R = context.active_object
            eye_R.name = 'VALVE_EYEDUMMY_R'
            bpy.app.handlers.scene_update_post.append(track_l_eye)
            bpy.app.handlers.scene_update_post.append(track_r_eye)
            bpy.ops.qceyes.popup('EXEC_DEFAULT')
        return {'FINISHED'}


attachment_string = '$Attachment "{name}" "{p_bone}" {x} {y} {z} absolute\n'
eyeball_string = 'eyeball {eyeball_side} "{p_bone}" {x} {y} {z} "{mat_name}" 3 {angle} "iris_unused" {size}\n'
flexcont_string = 'flexcontroller eyes range -{angle1} {angle2} {fc_type}\n'


class CleanBones(bpy.types.Operator):
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


class CleanBonesConstraints(bpy.types.Operator):
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


class QCEyesQCGenerator(bpy.types.Operator):
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


class QCEyesPopup(bpy.types.Operator):
    """Help popup"""
    bl_idname = "qceyes.popup"
    bl_label = "QC eyes how to use!"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = 400 * bpy.context.user_preferences.system.pixel_size
        status = context.window_manager.invoke_props_dialog(self,
                                                            width=width)
        return status

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
        bone = bone.parent
        chain.append(bone)
        if bone == start:
            break
    if chain[-1] != start:
        print('SOMETHING WENT WRONG!', chain)
    return chain


class RenameBoneChains(bpy.types.Operator):
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
            bones = context.selected_bones if context.selected_bones else context.selected_pose_bones
            current_chain = context.scene.BoneChains
            if not bones:
                self.report({"ERROR"}, "Did you read \"How to use?\"? I think No.")
                return {'FINISHED'}
            bones = find_line_of_sight(bones[0], bones[1])
            bone_names = bone_chain
            if current_chain in ['LARM', 'RARM', 'LLEG', 'RLEG']:
                if len(bones) == 3:
                    bone_names = bone_names[:-1]
            bone_names = bone_names[::-1]
            for n, bone in enumerate(bones):
                bone.name = name_dict[bone_names[n]]
            # start_bone = context.selected
        else:
            self.report({"ERROR"},
                        "What is this? {} is not armature! I need armature!".format(ob.type.lower().title()))
        return {'FINISHED'}


class RenameChainPopup(bpy.types.Operator):
    """Help popup"""
    bl_idname = "valve.renamechainpopup"
    bl_label = "How to use rename limb !"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = 400 * bpy.context.user_preferences.system.pixel_size
        status = context.window_manager.invoke_props_dialog(self,
                                                            width=width)
        return status

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
