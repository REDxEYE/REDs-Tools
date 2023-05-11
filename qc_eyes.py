##############################################################
# Purpose:
#   Mimica do qc_eyes.exe para Blender
#
#  por: Davi (Debiddo) Gooz
##############################################################
import bpy
from .tools_panel import View3DTools

class VALVE_PT_QcEyes(View3DTools, bpy.types.Panel):
    '''Visible painel at 3D Viewport'''
    #bl_idname = 'valve.qc_eyes'
    bl_label = 'Qc eyes tools'
    bl_parent_id = 'VALVE_PT_TOOLSPANEL'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()
        column = box.column(align=True)
        column.operator("valve.qc_eyes_popup")
        column.separator()
        column.label(text="Dummies Options")
        row = column.row(align=True)
        row.operator("valve.qc_eyes_create_dummies")
        row.operator("valve.qc_eyes_update")
        row = column.row(align=True)
        row.operator("valve.qc_eyes_generate", text="Eyelid")
        row.operator("valve.qc_eyes_generate", text="DmxEyelid")
        column.separator()
        if scn.Armature and bpy.data.objects[scn.Armature].type == "ARMATURE":
            row = column.row()
            row.label(text="Head Bone")
            row.prop_search(scn, "HeadBone", bpy.data.objects[scn.Armature].data, "bones", text="")

        column.label(text="Eyes Options")
        column = box.column()
        column.separator()
        column.prop(scn, 'LeftEye')
        column.prop(scn, 'RightEye')
        column.separator()
        column.prop_search(scn, 'LeftEyeMat', bpy.data, 'materials')
        column.prop_search(scn, 'RightEyeMat', bpy.data, 'materials')
        column.separator()
        row = column.row(align=True)
        row.label(text="eyes_updown")
        row.prop(scn, 'EyesUp', text="")
        row.prop(scn, 'EyesDown', text="")
        row = column.row(align=True)
        row.label(text="eyes_leftright")
        row.prop(scn, 'EyesLeft', text="")
        row.prop(scn, 'EyesRight', text="")
        column.separator()
        column.prop(scn, 'AngDev', text="Deviantion Angle")
        #if scn.HeadObject and bpy.data.objects[scn.HeadObject].type == "OBJECT":
        #    column = box.column()
        #    column.prop_search(scn, 'HeadObject', text='')
        #    column.separator()
        #column.separator()
        #column.prop(scn, 'DmxEyelidScale')
        column.separator()
        column.prop(scn, 'UpperLower')
        column.prop(scn, 'UpperNeutral')
        column.prop(scn, 'UpperRaiser')
        column.separator(factor=0.5)
        column.prop(scn, 'LowerLowerer')
        column.prop(scn, 'LowerNeutral')
        column.prop(scn, 'LowerRaiser')

def track_l_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_L']
    bpy.context.scene.LeftEye = obj.location

def track_r_eye(_):
    obj = bpy.data.objects['VALVE_EYEDUMMY_R']
    bpy.context.scene.RightEye = obj.location

def track_upper_eyelid_lower(_):
    obj = bpy.data.objects['VALVE_EYE_UPPER_LID_LOWERER']
    bpy.context.scene.UpperLower = obj.location.z

def track_upper_eyelid_neutral(_):
    obj = bpy.data.objects['VALVE_EYE_UPPER_LID_NEUTRAL']
    bpy.context.scene.UpperNeutral = obj.location.z

def track_upper_eyelid_raiser(_):
    obj = bpy.data.objects['VALVE_EYE_UPPER_LID_RAISER']
    bpy.context.scene.UpperRaiser = obj.location.z

def track_lowerer_eyelid_lower(_):
    obj = bpy.data.objects['VALVE_EYE_LOWER_LID_LOWERER']
    bpy.context.scene.LowerLowerer = obj.location.z

def track_lowerer_eyelid_neutral(_):
    obj = bpy.data.objects['VALVE_EYE_LOWER_LID_NEUTRAL']
    bpy.context.scene.LowerNeutral = obj.location.z

def track_lowerer_eyelid_raiser(_):
    obj = bpy.data.objects['VALVE_EYE_LOWER_LID_RAISER']
    bpy.context.scene.LowerRaiser = obj.location.z

class VALVE_OT_UpdateDepsGraphEyeDummies(bpy.types.Operator):
    '''This refresh graphs after a .blend file is reloaded or, when user try create new Eye Dummies'''
    bl_idname = "valve.qc_eyes_update"
    bl_label = "Update graph"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass
        if (
            bpy.data.objects.get('VALVE_EYEDUMMY_L', None)
            and bpy.data.objects.get('VALVE_EYEDUMMY_R', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_LOWERER', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_NEUTRAL', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_RAISER', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_LOWERER', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_NEUTRAL', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_RAISER', None)
        ):
            bpy.app.handlers.depsgraph_update_post.append(track_l_eye)
            bpy.app.handlers.depsgraph_update_post.append(track_r_eye)
            bpy.app.handlers.depsgraph_update_post.append(track_upper_eyelid_lower)
            bpy.app.handlers.depsgraph_update_post.append(track_upper_eyelid_neutral)
            bpy.app.handlers.depsgraph_update_post.append(track_upper_eyelid_raiser)
            bpy.app.handlers.depsgraph_update_post.append(track_lowerer_eyelid_lower)
            bpy.app.handlers.depsgraph_update_post.append(track_lowerer_eyelid_neutral)
            bpy.app.handlers.depsgraph_update_post.append(track_lowerer_eyelid_raiser)
            bpy.ops.valve.qc_eyes_popup('EXEC_DEFAULT')
        return {'FINISHED'}

def add_empty(name):
    bpy.ops.object.add(type='EMPTY')
    empty = bpy.context.active_object
    empty.show_name = True
    empty.name = name
    empty.empty_display_size = 0.5

def add_eye(name):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=0.5,rotation=(1.570796, 0, 0))
    bpy.context.object.data.name = 'VALVE_EYEDUMMY'
    eye = bpy.context.active_object
    eye.name = name
    eye.display_type = 'WIRE'
    eye.display.show_shadows = False
    eye.show_wire = True
    eye.show_all_edges = True

def bind_depsgraph(name):
    bpy.app.handlers.depsgraph_update_post.append(name)

class VALVE_OT_CreateEyeDummies(bpy.types.Operator):
    '''Create spheres to mimic qc_eyes.exe setup'''
    bl_idname = "valve.qc_eyes_create_dummies"
    bl_label = "Create"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass
        if not (
            bpy.data.objects.get('VALVE_EYEDUMMY_L', None)
            and bpy.data.objects.get('VALVE_EYEDUMMY_R', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_LOWERER', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_NEUTRAL', None)
            and bpy.data.objects.get('VALVE_EYE_UPPER_LID_RAISER', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_LOWERER', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_NEUTRAL', None)
            and bpy.data.objects.get('VALVE_EYE_LOWER_LID_RAISER', None)
        ):
            bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=0.5,rotation=(1.570796, 0, 0))
            bpy.context.object.data.name = 'VALVE_EYEDUMMY'
            eye = bpy.context.active_object
            eye.name = 'VALVE_EYEDUMMY_L'
            eye.display_type = 'WIRE'
            eye.display.show_shadows = False
            eye.show_wire = True
            eye.show_all_edges = True
            eye_mesh = bpy.data.meshes.get('VALVE_EYEDUMMY')
            eye_left = bpy.data.objects.get('VALVE_EYEDUMMY_L', eye_mesh)
            eye_right = bpy.data.objects.new('VALVE_EYEDUMMY_R', eye_mesh)
            bpy.context.scene.collection.objects.link(eye_right)
            eye = bpy.data.objects['VALVE_EYEDUMMY_R']
            eye.display_type = 'WIRE'
            eye.display.show_shadows = False
            eye.show_wire = True
            eye.show_all_edges = True
            add_empty(name='VALVE_EYE_UPPER_LID_LOWERER')
            add_empty(name='VALVE_EYE_UPPER_LID_NEUTRAL')
            add_empty(name='VALVE_EYE_UPPER_LID_RAISER')
            add_empty(name='VALVE_EYE_LOWER_LID_LOWERER')
            add_empty(name='VALVE_EYE_LOWER_LID_NEUTRAL')
            add_empty(name='VALVE_EYE_LOWER_LID_RAISER')
            bind_depsgraph(name=track_l_eye)
            bind_depsgraph(name=track_r_eye)
            bind_depsgraph(name=track_upper_eyelid_lower)
            bind_depsgraph(name=track_upper_eyelid_neutral)
            bind_depsgraph(name=track_upper_eyelid_raiser)
            bind_depsgraph(name=track_lowerer_eyelid_lower)
            bind_depsgraph(name=track_lowerer_eyelid_neutral)
            bind_depsgraph(name=track_lowerer_eyelid_raiser)
            bpy.ops.valve.qc_eyes_popup('EXEC_DEFAULT')
        return {'FINISHED'}

attachment_string = '$Attachment "{name}" "{p_bone}" {x} {y} {z} absolute\n'
eyeball_string = 'eyeball {eyeball_side} "{p_bone}" {x} {y} {z} "{mat_name}" {radius} {angle} "none" {size}\n'
flexcont_string = 'flexcontroller eyes range -{angle1} {angle2} {fc_type}\n'
dmxeyelid_string = 'DMXEyelid {eyelid_side} "{head_obj}" lowerer "{lower_shape}" {lid_pos1} neutral "{neutral_shape}" {lid_pos2} raiser "{raiser_shape}" {lid_pos3} righteyeball righteye lefteyeball lefteye\n'

class VALVE_OT_QCEyesQCGenerator(bpy.types.Operator):
    '''write qc_eyes.qci file based on configuration'''
    bl_idname = "valve.qc_eyes_generate"
    bl_label = "Generate QC string"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        eye_l = bpy.data.objects.get('VALVE_EYEDUMMY_L', None)
        eye_r = bpy.data.objects.get('VALVE_EYEDUMMY_R', None)
        upper_lid_pos1 = bpy.data.objects.get('VALVE_EYE_UPPER_LID_LOWERER', None)
        upper_lid_pos2 = bpy.data.objects.get('VALVE_EYE_UPPER_LID_NEUTRAL', None)
        upper_lid_pos3 = bpy.data.objects.get('VALVE_EYE_UPPER_LID_RAISER', None)
        lower_lid_pos1 = bpy.data.objects.get('VALVE_EYE_LOWER_LID_LOWERER', None)
        lower_lid_pos2 = bpy.data.objects.get('VALVE_EYE_LOWER_LID_NEUTRAL', None)
        lower_lid_pos3 = bpy.data.objects.get('VALVE_EYE_LOWER_LID_RAISER', None)

        arm = bpy.context.scene.Armature
        if not arm or not arm in bpy.data.objects:
            self.report({"ERROR"}, "Armature not found, please set it up")
            return {'FINISHED'}

        if str(bpy.context.scene.HeadObject) == "":
            self.report({"ERROR"}, "Can't find any Head Object, did you set one?")
            return {'FINISHED'}
        else:
            head_obj = bpy.data.objects[str(bpy.context.scene.HeadObject)]

        head_bone = bpy.context.scene.HeadBone
        if not head_bone or not head_bone in bpy.data.objects[arm].data.bones:
            self.report({"ERROR"}, "Head bone not found in the armature, please set it up")
            return {'FINISHED'}
        else:
            p_bone = bpy.data.objects[str(arm)].data.bones[str(head_bone)]

        if eye_l and eye_r and upper_lid_pos1 and upper_lid_pos2 and upper_lid_pos3 and lower_lid_pos1 and lower_lid_pos2 and lower_lid_pos3:
            if not bpy.data.texts.get("qc_eyes.qci", None):
                qc_string = bpy.data.texts.new('qc_eyes.qci')
            else:
                qc_string = bpy.data.texts['qc_eyes.qci']
            qc_string.write(attachment_string.format(name="eyes",
                                                     p_bone=p_bone.name,
                                                     x=abs(eye_r.location.x) - abs(eye_l.location.x),
                                                     y=avg(eye_l.location.y, eye_r.location.y),
                                                     z=avg(eye_l.location.z, eye_r.location.z)))
            qc_string.write(attachment_string.format(name="righteye",
                                                     p_bone=p_bone.name,
                                                     x=eye_r.location.x,
                                                     y=eye_r.location.y,
                                                     z=eye_r.location.z))
            qc_string.write(attachment_string.format(name="lefteye",
                                                     p_bone=p_bone.name,
                                                     x=eye_l.location.x,
                                                     y=eye_l.location.y,
                                                     z=eye_l.location.z))
            qc_string.write('\n')
            qc_string.write(eyeball_string.format(eyeball_side="righteye",
                                                  p_bone=p_bone.name,
                                                  x=eye_r.location.x,
                                                  y=eye_r.location.y,
                                                  z=eye_r.location.z,
                                                  radius=avg(eye_r.scale.x, eye_r.scale.y, eye_r.scale.z),
                                                  mat_name=bpy.context.scene.RightEyeMat,
                                                  angle=bpy.context.scene.AngDev,
                                                  size=avg(eye_r.scale.x, eye_r.scale.y, eye_r.scale.z) * 0.5))
            qc_string.write(eyeball_string.format(eyeball_side="lefteye",
                                                  p_bone=p_bone.name,
                                                  x=eye_l.location.x,
                                                  y=eye_l.location.y,
                                                  z=eye_l.location.z,
                                                  radius=avg(eye_l.scale.x, eye_l.scale.y, eye_l.scale.z),
                                                  mat_name=bpy.context.scene.LeftEyeMat,
                                                  angle=-bpy.context.scene.AngDev,
                                                  size=avg(eye_l.scale.x, eye_l.scale.y, eye_l.scale.z) * 0.5))
            qc_string.write('\n')
            qc_string.write(dmxeyelid_string.format(eyelid_side="upper",
                                                    head_obj=head_obj.name,
                                                    lower_shape='EM64', 
                                                    neutral_shape='AU0', 
                                                    raiser_shape='EM63',
                                                    lid_pos1=upper_lid_pos1.location.z - avg(eye_r.location.z, eye_l.location.z),
                                                    lid_pos2=upper_lid_pos2.location.z - avg(eye_r.location.z, eye_l.location.z),
                                                    lid_pos3=upper_lid_pos3.location.z - avg(eye_r.location.z, eye_l.location.z)))
            qc_string.write(dmxeyelid_string.format(eyelid_side="lower",
                                                    head_obj=head_obj.name,
                                                    lower_shape='EM64', 
                                                    neutral_shape='AU0', 
                                                    raiser_shape='EM63',
                                                    lid_pos1=lower_lid_pos1.location.z - avg(eye_r.location.z, eye_l.location.z),
                                                    lid_pos2=lower_lid_pos2.location.z - avg(eye_r.location.z, eye_l.location.z),
                                                    lid_pos3=lower_lid_pos3.location.z - avg(eye_r.location.z, eye_l.location.z)))
            qc_string.write('\n')

            qc_string.write(
                flexcont_string.format(
                angle1=bpy.context.scene.EyesUp,
                angle2=bpy.context.scene.EyesDown,
                fc_type='eyes_updown'))
            qc_string.write(
                flexcont_string.format(
                angle1=bpy.context.scene.EyesRight,
                angle2=bpy.context.scene.EyesLeft,
                fc_type='eyes_rightleft'))
        else:
            self.report({"ERROR"},
                        "Can't find eye dummies, did ya create 'em?")
        return {'FINISHED'}

def avg(*args):
    return sum(args) / len(args)

class VALVE_OT_QCEyesPopup(bpy.types.Operator):
    '''Help popup for qc_eyes'''
    bl_idname = "valve.qc_eyes_popup"
    bl_label = "QC eyes how to use!"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        width = int(400 * bpy.context.preferences.system.pixel_size)
        return context.window_manager.invoke_props_dialog(self, width=width)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="How to use!")
        col = box.column(align=True)
        col.label(text="Place both dummies where eyes supposed to be")
        col.separator()
        col.label(text="Apply eyes materials to them")
        col.label(text="After all this trash click \"Generate QC\"")

    def execute(self, context):
        return {'FINISHED'}
