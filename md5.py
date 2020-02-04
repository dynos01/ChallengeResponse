def md5(data):
    buffer = bytearray(data.encode())
    bufferLength = len(buffer)
    buffer.append(0x80)
    x = (bufferLength - 55) // 64 if (bufferLength - 55) % 64 == 0 \
    else (bufferLength - 55) // 64 + 1
    buffer.extend(b"\x00" * (64 * x + 55 - bufferLength))
    buffer.extend((bufferLength * 8).to_bytes(8, "little"))
    consts = [3614090360, 3905402710, 606105819, 3250441966, 4118548399,\
    1200080426, 2821735955, 4249261313, 1770035416, 2336552879, 4294925233, \
    2304563134, 1804603682, 4254626195, 2792965006, 1236535329, 4129170786, \
    3225465664, 643717713, 3921069994, 3593408605, 38016083, 3634488961, \
    3889429448, 568446438, 3275163606, 4107603335, 1163531501, 2850285829, \
    4243563512, 1735328473, 2368359562, 4294588738, 2272392833, 1839030562, \
    4259657740, 2763975236, 1272893353, 4139469664, 3200236656, 681279174, \
    3936430074, 3572445317, 76029189, 3654602809, 3873151461, 530742520, \
    3299628645, 4096336452, 1126891415, 2878612391, 4237533241, 1700485571, \
    2399980690, 4293915773, 2240044497, 1873313359, 4264355552, 2734768916, \
    1309151649, 4149444226, 3174756917, 718787259, 3951481745]
    rotateVars = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, \
    5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 4, 11, 16, \
    23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, \
    15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    initVars = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
    for chunkIndex in range(0, len(buffer), 64):
        h0, h1, h2, h3 = initVars
        chunk = buffer[chunkIndex:chunkIndex + 64]
        for i in range(64):
            if 0 <= i < 16:
                r0 = (h1 & h2) | (~h1 & h3)
            elif 16 <= i < 32:
                r0 = (h3 & h1) | (~h3 & h2)
            elif 32 <= i < 48:
                r0 = h1 ^ h2 ^ h3
            else:
                r0 = h2 ^ (h1 | ~h3)
            if 0 <= i < 16:
                r1 = i
            elif 16 <= i < 32:
                r1 = (5 * i + 1) % 16
            elif 32 <= i < 48:
                r1 = (3 * i + 5) % 16
            else:
                r1 = (7 * i) % 16
            rotateObj = (h0 + r0 + consts[i] + \
            int.from_bytes(chunk[4 * r1:4 * r1 + 4], "little")) & 0xFFFFFFFF
            rotated = (h1 + ((rotateObj << rotateVars[i]) | \
            (rotateObj >> (32 - rotateVars[i]))) & 0xFFFFFFFF) & 0xFFFFFFFF
            h0, h1, h2, h3 = h3, rotated, h1, h2
        for i, j in enumerate([h0, h1, h2, h3]):
            initVars[i] = (initVars[i] + j) & 0xFFFFFFFF
    md5 = sum(j << (32 * i) for i, j in enumerate(initVars))
    return "{:032x}".format(int.from_bytes(md5.to_bytes(16, "little"), "big"))
