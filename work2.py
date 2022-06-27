def int32_to_ip(int32):
    r = str(int32//(256**3))+'.'+str((int32%(256**3))//(256**2))+'.'+str((int32%(256**2))//256)+'.'+str((int32%256))
    return r
