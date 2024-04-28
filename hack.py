from pymem import Pymem
from pymem.ptypes import RemotePointer

import keyboard

pm = Pymem("GodotSeaven_GDK_desktop.exe")

offsets = [0x148,0x140,0x108,0x28,0x58,0x20,0x200]

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
while not keyboard.is_pressed('q'):
        pm.write_int(getPointerAddress(pm.base_address + 0x03674F10,offsets=offsets),1000)