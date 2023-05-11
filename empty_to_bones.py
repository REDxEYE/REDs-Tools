import bpy
from .operators import enable_if, get_edit_bone, get_pose_bone, mat3_to_vec_roll

class ARMATURE_OT_empty_to_armature(bpy.types.Operator):
    """Convert the selected empties to bones. Bones are constrained to empties, then can be baked (search for NLA bake function in the F3 search menu)"""
    bl_idname = "armature.empty_to_bones"
    bl_label = "Empty to Armature"
    bl_options = {'UNDO'}

    @classmethod
    def poll(self, context):
        enable_if(context, 'EMPTY')
           
    def execute(self, context):
        use_global_undo = context.preferences.edit.use_global_undo
        context.preferences.edit.use_global_undo = False
        try:
            create_armature()
        finally:
            context.preferences.edit.use_global_undo = use_global_undo
        return {'FINISHED'}


def create_armature():    
    '''This is something made to aid miHoYo's armature import in Blender.'''
    # store selected empties
    empties = [i.name for i in bpy.context.selected_objects if i.type == "EMPTY"]

    # make a new armature at scene origin
    bpy.ops.object.armature_add(enter_editmode=False, location=(0, 0, 0), rotation=(0,0,0))
    name = bpy.context.active_object.name
    arm = bpy.data.objects.get(name)

    # delete the default bone
    bpy.ops.object.mode_set(mode='EDIT')
    b = arm.data.edit_bones[0]
    arm.data.edit_bones.remove(b)

    bone_list = {}
    # create bones from empties
    for empty in empties:
        emp = bpy.data.objects.get(empty)
        vec, roll = mat3_to_vec_roll(emp.matrix_world.to_3x3())
        nb = arm.data.edit_bones.new(empty)
        # align
        nb.head = emp.matrix_world.to_translation()
        nb.tail = nb.head + (vec)
        nb.roll = roll

        # store empties hierarchy at bone_list
        parent = None
        if emp.parent:
            parent = emp.parent.name
        bone_list[empty] = parent

    # use bone_list to parent bones
    for b in bone_list:
        parent_name = bone_list[b]
        if parent_name == None:
            continue
        parent = get_edit_bone(parent_name)
        if parent:
            get_edit_bone(b).parent = parent
            
    # constrain bones for bake animations (optional)
    bpy.ops.object.mode_set(mode='POSE')
    for b in bone_list:
        bn = get_pose_bone(b)
        constraint = bn.constraints.new("COPY_LOCATION")
        emp = bpy.data.objects.get(b)
        constraint.target = emp
        
        constraint = bn.constraints.new("COPY_ROTATION")
        emp = bpy.data.objects.get(b)
        constraint.target = emp
