#zafck。抓ucode-openapi.aax6.cn下的token不要Bearer 多账号& 增加失效通知和领会员通知

import sys
from packaging.version import parse as parse_version
Npyvs = '3.10'
Ypyvs = sys.version.split()[0]
if parse_version(Ypyvs) >= parse_version(Npyvs):
	print(f'当前py版本:{Ypyvs}可运行')
else:
	print(f'py版本为{Ypyvs}不支持运行脚本,需要py版本为{Npyvs}及以上')
	exit(0)
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\x9dW9\xce\xecHr~\xaf\xfb\xf5L\xab\r\xddcPF\x91,V\x15\t\x08\x82\x92kq/\xee\x8b#$\x97\xe2\xbe\x93\xc5\xc5\x9d+\xe8\x003\xa6|\x01\x82\xae\xf2\xdb\x921\x07\x18\x7f\xf8\xfen\x8c!\xc8R\x02\x11_\x92\x91\x0b"2"3"\xfa\xf2\xbf\xda\xef\x0e\xfa\x97\x83\xc6\xc7\xc1\xe2/\xf1\xd7\xeaK\xf0+~\r\xbe~\xe2\x0f\xc1\x0f\x9f\xf8c\xf0\xe3\'~\x0b\xbe}\xe2O\xc1O\xc9\xef\x92/\x7f\xfa}\xf2\xedO?\xc7?\xfc\xf9\xeb\x9f\xbf\xfe\xf1\xeb\xd7Cb~\xf9\xc3\x8f\x7f\xf9\xbe\xb6:\xda\xff\xf8\xe5\x8b\xbf\x80\xff\xab\xf1\xdf\x99\xfe\x9d=T\xe1;\x04\x80*\x81\xbb\x007=\x90\xd7\xa9\x10p\x10\xb8\xfa\xf1\x9f\x1bA\xd5\xd2\xbf\xc9\x197U\x7f\x93\x1b\x90\xe2\x7f\x95SN\xcb\x05zP\x01\t<\x02]Ki^\xa7[\x9d\xcf\x80\xafP@?\xe69\n\x90\xf4g\xf7\xb93{\xdd\xb1\xa5<P\x84\x90)W\xdd)k\x1b\xad#L\xbf\x15\x00\x18\xf4\xeb\xfc\xf7v9\xe8}>\xc3\xcf\xfe\xeb\xfc)\xb9\x90\xaf\x13\xd0i`x\xa7\x9cf1 (\xde%\x9d}\x10\xc1i*\xd4\xde\xee\xb1Y\x1e\x83\xd0\x87\x82n\x93=\x10\xfb\xd02\x9eFo-+_ \xb6\xb2)}\xd2>\xfa\xa4\xd0aa!M\xaf\xd4H\xd3\x1a\xb7:+}\x08\xb2\x92\xb4P@Zb\xf9\xd4\xb1\x16\x11\xb0<i\x81\x0fj\xfd\xd1\xab\xad\xca\xd6\x02\xa8\xcd\xd0L(\xcb\x82\x8e\x8a\xdb\xe8s\xb3\xb1v\xe3u\x06}JO\x1b\xf2\xe8\xd3\xe6\xd3G\x7f\xe8\xc8\x1c&U\xf9\x14\x01\x88\xca\x17,`\x0eCC\xbf\xd6\x01\xe4\xebZW\x8c\xaee\x84\x8d\x11\xa0"\xb6\xd4\xd1e\x04%U\n\x01\x81\x00\x01J\n\x19]=\x0c\x0c\xc0\xa2+\xb5\xd1\xf2)PLJ\xcc\x94\xcc\x12\x0b\xd3/\xf4\x95\x0eM\xbfN\x91\r\xf2\x82"@@\xb5\xe0\x93>\x19\xf2\xeb\xe92\xfa\xffw/\xd1\x10\x04\x0bZ\x96\x00S\x9fEH\xcbh\xc1\xa1\x11\x9f\xb5\xbf\xad\xacR]\xbb\xfd\xaa\xd0\xa7\x1b\x1d\x86\xa4\xba\xba\xbbY\xe7\x043K\xc6\xa2\xb3\xca\x89\xacA\xb6tWG\xed8\x99}S\xe6N3a\xa3\xaepm\xae^\x03\x14!y\xcb\x9e\\\xe2\xcfm{\xa1E\xb9\xf5Y\xd4\xe4Y\xbdX\r\x9bs\xc2;\xbb\xc8\xd9\xb6)\xa9\xeb\xa4\xbc\xad\xf8T\xda\\\xeeS\xbce\xbc\x1es\xb9\x12PV\xc1\x9a\xa1\xe1^\x88\xb7c\xa1Nw\xdaP\xb40\xf3\x9d\x04\x85\xe2\t\xbd\xfa\x9e\xbb\xe7\xe5\xfc~\xc2\x17:q&NZ\xb1X"\xb54m\xa2<7i0\xec~\xc3\xe7\xfa\xb9\x17z1ZX\xd0.\xba\xc0jE\xc9?eQ\xd0\xe8\xba\xa2\xd2,\xa4ls\xb0\xf9\x8a\xbb,\xd2\x02\xb0\xbc\x1cs~\xa4\xbb\xfe!\xa1\x0f\xc7\x11\xa2\xc1\xd4\xe5k\xa4\xd5\xcd\xadnRqSw\xe3\r$$\xa1\x18@\x1aJIn\xd1\xb5\x0ezC\xa7\x120P\xfcFK\xd6\xa5e\x9bK\xa9\x83H\x045\xb3\xe4\xeb\xda\x80W\x8dg\x03\x9d\xa3\x80-BSx\x99\x8b?\x869\xe8\x94\x1cP\x13P\x87]\xe2/\x13\x96\n\x03M\xab9\x88\xa2\xb7[-\\5\xb4\'l3\xa9D\xa7Y\x94\xd2\x11!\x18\xab\x87\xa9\xb6\x17\xb5\xa26H\xfb\x0b\xa3\xa7\xc5\x84?K\x90\xf1\x0c\xf0@K\xdb[,\x00\x03\x04Z\x98tt~\xb2#\x01\n\xd7\xc7\xe0\x99)Gg\xd0\xbc\xa5\x97\xe7,\xf1$\x95\xda\xb52+\xa4f\xa9\xf4\xd2\xb29\xef\xc9>G\xeb\xacU\x8a\x902\x99\xce\x97\xab\x06\x99\xca9\xbb\x15o\xc90\xa3\xcc\xa4mp\xed"<\xef\xdc#\xd6\xa6M\x896Fg\x82\x80I\x10\xd0\xd5l\xef\x0b\xbe\xbbE@)S\x84\xcd\x97\xc0I\xd5\x9dq\x03\xb2e\x16\xc5\xafsB\x06\xcf\xfbT\x0f\xefPaw\x9d\xb1sA\xcd}\xc5\xabF\xc6\xf3\x87L\x85{\xde\xd4\t\xd6\xb7\x0b\n\x84\xecPA\\\xa6g\xc5\xe1\x10\x82D\xbd\xd38\x13;(K\xb31\xb6\xb4\x04L\xd5p\x1a3\xdda\x98B\xa4\xc1\xa4q\xe3\xe8j\x82\x14\xcdo\xd9^\r.\xaa\\\xd4\x81\x9c\x1f\xc9\xc3\xcd\x9bS\x88\xa3y\xca\x9f\x96Q\xbe\xdfF5k\x9ct\xa6\tv\xd1}\xb9F\xa2u\x07;\xe3\xfb1F\xa6c\x18_q:R\xe8$\xa2I#\xd1KN\xad.@\x89\xf1\xb6\xef\x99\xaeo\xc5\x86\xf2u\xe8\xe04\x12\x83\x81\xf1\xcb\x92\xe1/\xfa\xcaY"\xaa]\xfb\\\x96n\xef\xa1\x07\xa9\xd7\xe7\x88\x88E\x8f\x93\x1c\x08\x99\x84E(\x9dI\xeed\x8c\r\xdd\xf1\xa2\x07(Ysv\xd4\x01\x82\xb5r\xdb\xda\xd8\xcf\x9a\xc17QY\xc5\xfcT\xd2\x16\x1f\x19T\x99,vL\x14|\x9c\xb6\xa6K\xe9e\x96O\xb5\xd1\xf4\rK\xe0\xfel?\x1eg/\x11\xa9\xa6`\xf5\xe8Z\xc4\x93\x02\xc8\xfb\x83B\xcbH\xbdN\x12.\xb9\x81KV\x89\x84\xcac\x18\xaal\xb6\xb17e\xc7\xa8\xe5\x95\xdd\x866a\xa7\xfb\xa0E\xe6<&<\x8a$\x04\xeeq\xfb<\x81\xdd\x7f$E\xb1Yg\xd8C\x8a+\xef\'s\xe0\x87\x04\xe02]_\x87\xf0\xda\xb3\x15\x06(\xd1|\x8e\x8a\x08\x94\xb5&^\xd2U\x96w7\xbd\x0e\x98H\xf4d\xec:Z\x9b\x97\xb7\xb7\x88\xde1S\xef\x07\x88h\xef\xe9\xddn9\x7f\x13\x04\x900a\xaa17\xa7\xe7=\x81\xab+\xe6t<$"g\xb8W\x90.WS\xf0\xb3\xe4T\x99\xe9\xb2\x13I,\xe1\xc8\x9a\x9d.Vx\xd2a\xbc\xae\xd1\xa8\xa3\xf7Q^1K\xdf\xb2\xac\'\x81\xee\x0e:\x1f\x83J\xad&"\x93p\xbb\x11\xf7\x1b\x8d 2=]^5\xd9\xbdi(\x18\xae\x10\x96\xd3\x99\xb4{\xae\x87p=q\xda8<.d\xf4\x06\xf9bLO^B\xdb\x11\xc6\xbb\xdc\xb5o\x86{X\x8e\xf6dgFL\xda\xb7\xec\xd3\'\x95\xa5<\x97\xbf\x93\xb7\xeb\xde\xcd\xd0m\x19`\xf6\xa7,\xb3\xbd\x8a\xf1\x91\xd9} a<\x93\x9e\tT\xbah"\x9eI\xc3\xf9}\x15\x97\xcdQ\xf2+\xd3H\x17m\x1a\x9a\xc1V\xc4\xcc\x91\xb7&\xb8\xd0\x08v[oO\xb9\x07Z\xa7\x05{+\xc0\xb6\xe1\xd5;%=f\xe7rD\xd2.LI8\xdd\xc6,\x94\x8e\xfb\xd2\x97\xe6w3\r\xd5\xce=\x97\x93?\x1a;\x1c\xe0\xc6\xd9,\xb3\xd8\xfc\\\xa5^\xc3r\x14\xb1\xac~\x18\x82\x9d\x0b4\t\x18\xf8c\xf4\t\xd4\r\xcd\x10\xe7\x035/\x03$\xcf\xed\x88\xae\xc6\xc6\x0c\nJ\xca\x94=)w6H\x9c\xebY\x08wu2\xed\x95\xdd\x9b*\xe7u\xf8\xb2FRV\xab\xce3\xeaP\xa5cQ\x1d\xf5[\x12\x1fQ\x12\xd3\xe8\x1bO<#\xdc\xc5\xeb39%\xca\x1d\x17*\xbd\xbc\xd1\xd4\xa5>\xae*vS\xc8\xfe\x1e!1\xcb\xb8\x9d\xc6\xd0(\xe3K\x9d\x03\xe57qF\xf7\x19\xc9\x9bp:swI\xd8\x88\x8e\x10\x94%SI\xfal\x97\xbb\xa3\xd2\x92}~\xe8\xdep\xcb\xa6\xd01\x12%\x11\xc6A\xac:B\x87\xf4\x03e\x0c\x0cvs\xa5\xe2\xa7\xc9\xd64^5-\x92\x91\xbcB\xbd$\x9e\x9c\x08a\xedc\x93\x9bg\x8b\x18\xd0\x82\xdf\xaa\xc2\xceG.+34\xde=\xe8}!\x04\xcdF\x92\x12\xcbs>\x1b\xc5I\xd2b\x8cU\xe8\\6\x9c\xa7\x94LlF\xdd\x90\xb1\x11\xd6>^\x06\xdcN\xb1\x06\xf0oM[\x05\\\xa4y\xfb\x1e\\K\x15\x9c\xf4@\x95u.\x100\x14\x7f\xd3V.\x12wE\xc4y\x82\x1bo>\'Ny\xc0X\xc6Bd\x0f\x1a\'\xb0\x9b\xae#|\xa2@\x13Ow\x12\x1dx0Y8\xdb\x14\x1a\x80d^qw5\xa9\xfd\xec\xf4t\x1f\x82\xa1\x92Z\x0c\xac\xe7\xe5\xea\xf4b\xca\xd3r\xa9F\x84\x99\x99\xd3\xd3\xa0\xb0vQz\x83\xc7\xedef\xd4\x95\xe5\xdaB\x89\x1f>S\xc0\x91\xce\xd9\xc6\xa1\x02B\xd7\xfd\xa0\xf7\xda\r\xcd\x07e]\xe1I\xc17\xea\xaa\x9a\x1b\xb3d{\x1c\x15T\x8f\x8eXu"\xae\x1a\x05T\xb9\x8d\x99\xea9-\xb3(\xbe\xc5}\xcf`\xbe\x82\xd0V\xf3\xd9\x97\xadPqD\\)i8\xbb%\x8e^\xc7\t#\x02\x9a\xe2\x0e\x17(\xc6\x12(*\xdd\xb1\xab\xb3\xb7<\x98{\x86:\xde\x06%\x92\xee\xd2\n\xf5\tA\xb0\x8a\xc7\xba\x91P\xcd\xbc\x82\xbc\x1b\xea\x1c\xb1\xd1\xa9\x14\xb8\xb7\xac \xe7E\x08\x95t\xe7\xc3z\x05\x8e\xbfH\xee\xda\xa8\t\xc4\x85g\x1b\x05\x01q\xbd\xe4\x927rY\xae\x95\xefQ\x10o\xd8\xdc\xc3\xd4i\x9f\xadp;LI\x17\x8fa\xd9E_\xb8\x85U\xc8\x87 b\x86\x8d\xd6/\x19\x88V\xd1f\xd0f}\xb4w\xf7\xea"w1\x1d\x194\xc1{E\xbdk\x86\xdc\x9el\x0e\xc0+\xc7:\xea)\xe2\x87x\x80\xa9-S=\x02J3\x8f1$\xcd^\x98E6\xfe\xb2\x92A\xb0\xd5!=O\xc5+>\xafKM\xa8O\xf0\xea\xdc\xd3\x9d\xc5\x8aF`,\xdc\x7f\xaf\x134A\x11\x1a\x96w\xd1KJc;\x8e\xa9\x1d\xe8\x08\xe1\x91\xdc47\xbd\x10\xdf\x0e\x9c\xca\xa6P&\xc9\xf0XBJ\xc8\xa4\x89\xf3\xe0\x91\x02R\x11\x88\x82\xd3}I\x04\x9c\xe1INqd\xc4\xb8y\x03\xa7\x816\xb9\xd6Y-\xaa\xf4\xf4\x8c!\x0f\xbfa\x92\xb8\xda\r\x8b\xb9)\xf80N\x00\xa2\xe3\x92I\xcc\xe9%r\xa7N-\x11\xad-[\xdf1F4<\xeb+\x8f\xf5\xb3P\x1a\xadtj\x8e\x8c\x8bJ^\xd0x\xb5\x1au_1(\xd6^^\x95N\x8aT\xb5s\xaeimS\x88`y\xe6N\xeb\xba/\x89\x12\xccBaa\xe8\xb7\xa35*\xc7\xb5\x1b!<\rE\xff|5}[g\x17\xb1T\xdeZ\xaa\xc2\xea\xaa\xad\x05s\xa5F-\'\xc4\xb0\xf3\x1bbE\x84\xa5\x01\xefwG\xf5wY\xbb\xc7\xa0\x1c\xb3k\xf1N\x8f\xf0\xf1-\x7f\xa5\xef\\Y\xa5V\xffP\x99\xaeb\xa5\xb8M\xcb\xebs\xf0K\xd2\xbe\x86\xfdU\xb5\xcb\xc6}-\x9b\xb6\x98<+2\x08kGPF\\\xbf\xed\x04\x83[)zt7\x1a\xb6\xaf\xfc\xad\x0b\xa6\xd6\\\x8d\xdeV3\x96\xca\xf2J@\xb8\xb4\xd5\x9eT\x86t"\xc0\xb8^8\xf9n\x8b\x1d\xc9jF\x99\xc0\xf2Y\x81]\xb4\xd5\xf7]\x8c\x0c}\x0f\xcc\xcfp<[\xaa\xde\xf89\xa5\xcfu\x9c\x87\x05m\xe9\x18V\x8ajr\xd1\xe5\xe8\xdeP$*xK}\xc9\xc5\r\xf3&\x99\xd1\xb7\\\x93Q*\x14\xfb\x9dC\x9ej\xa7e\x08\xd5<\x01\xb1;\xe9\xf1\xf4N"=\x80;\xaa;\xab\xa8\xdcNYh/\xa3\xa7Z^\xd6\xed\xa7\xac\x93z\xf5\xd1\xcd\xbcG\t\xcb\xdd\xb0\x96\xbb\x89\x0b\x88\x9a-q/sE6F\x9e\xe5)\xaa5R\xefshE\x9a\xd6X>\xa7\'\xc5\xe5\x149\x08\x8af\xfb\xd9N}\x80\xd8>\xb6+\xa5/ea\xea\xde[\x02\x94\xeaJ\xe5\xb7\xc7h\xe1w!\xbd\xc1\xb9\xca#\xaei\x9f\x0b\xc2\x13\xce\xb3I\xf9\xba\xf2\x90\xe1\xfc\xf0\x89\xe7I\x9eM)\x92\xd8L\x0b\x85\xd8H\xe9R\xc4\xd2x\xf2=q\x87<7b\xa91&5\x9a\x1d\xd8$u\xb5`\xa9\x9a\'\x85\x0ci^\xec\xc2\x9a\xdb}\xac\xea\x0e\xd9-\xe4\xab\xfc\xc0*\xe1\x9d\x02K\x9d1\xc4\xb82"[)8\xbeC\x0c]\xa2\xda\xd9\xa3[\t\xa2\xf4\xb3n8\xe2\xf9\x80\xa3x\xf9\x9e\xd1_\xe5\xfa8\xdb\x04\xc1\xd2\x94\x08]\xb2\x8c\xdd\xb5z\xa6\xec\xf7q;\xf8>\x8eM\xc1/\x7f\xf8\x87\x8f\xdf\xd7p\x183X}|\xab\xf6\x1a~|K\xf7\xbc\xfb\xf81\xdc\xb1\x8f\x9f\xc3\xbc\x81c\x94\xe7\x1f\xdf\xf6*\x0f?\xbe%k\x12}\xfcT\xb50\x1e?~\x81X\xf8\xaf!\x1c\x93\x1b\xfe\xef_\x86_\x8e2\xf5\x93\xfd\xf5{!\xfc\xdf\xff\xf5o\xff\xf3\x9f\xff\xf1\xf1\xf3?\xd5m<W\xc9?\x7f\xfd^\x18\xffp\xb0\xc7\x97\xbf\x01Pz\xfc\xb6')))
except KeyboardInterrupt:
	exit()