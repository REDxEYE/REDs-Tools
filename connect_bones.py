import bpy
import mathutils

bpy.ops.object.mode_set(mode='EDIT')
for bone_ in bpy.context.selected_editable_bones:

    if bone_.parent:
        parent = bone_.parent
        if len(parent.children) > 1:
            bone_.use_connect = False
            parent.tail = sum([ch.head for ch in parent.children], mathutils.Vector()) / len(parent.children)
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
