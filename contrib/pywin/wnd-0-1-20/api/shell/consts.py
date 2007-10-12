
#***************************************************
# special folder constants - use with Desktop.ListSpecialFolder
CLSIDL_DESKTOP = 0
CLSIDL_INTERNET = 1
CLSIDL_PROGRAMS = 2
CLSIDL_CONTROLS = 3
CLSIDL_PRINTERS = 4
CLSIDL_PERSONAL = 5
CLSIDL_FAVORITES = 6
CLSIDL_STARTUP = 7
CLSIDL_RECENT = 8
CLSIDL_SENDTO = 9
CLSIDL_BITBUCKET = 10
CLSIDL_STARTMENU = 11
CLSIDL_DESKTOPDIRECTORY = 16
CLSIDL_DRIVES = 17
CLSIDL_NETWORK = 18
CLSIDL_NETHOOD = 19
CLSIDL_FONTS = 20
CLSIDL_TEMPLATES = 21
CLSIDL_COMMON_STARTMENU = 22
CLSIDL_COMMON_PROGRAMS = 23
CLSIDL_COMMON_STARTUP = 24
CLSIDL_COMMON_DESKTOPDIRECTORY = 25
CLSIDL_APPDATA = 26
CLSIDL_PRINTHOOD = 27
CLSIDL_ALTSTARTUP = 29
CLSIDL_COMMON_ALTSTARTUP = 30
CLSIDL_COMMON_FAVORITES = 31
CLSIDL_INTERNET_CACHE = 32
CLSIDL_COOKIES = 33
CLSIDL_HISTORY = 34

# felt free to define these
# TODO: kick out, not needed
USERCOMP_NAME = 0	# compare pIdls by name
USERCOMP_EXT = 1		# compare pIdls by extension

SPECIAL_FOLDERS = (0,1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,
20,21,22,23,24,25,26,27,29,30,31,32,33,34)


## file attributes
SFGAO_READONLY      =    0x00040000
SFGAO_FOLDER      =     0x20000000
SFGAO_FILESYSTEM    =    0x40000000
SFGAO_REMOVABLE     =    0x02000000
SFGAO_LINK       =       0x00010000
SFGAO_HIDDEN    =    0x00080000
SFGAO_SHARE   =          0x00020000L
SFGAO_DROPTARGET    =    0x00000100
SFGAO_NONENUMERATED =    0x00100000L
SFGAO_BROWSABLE    =     0x08000000
SFGAO_COMPRESSED   =     0x04000000
SFGAO_NEWCONTENT   =     0x00200000L
SFGAO_GHOSTED      =     0x00080000L
SFGAO_HASPROPSHEET   =   0x00000040
SFGAO_HASSUBFOLDER   =  -2147483648
SFGAO_FILESYSANCESTOR =  0x10000000
SFGAO_CANRENAME   =      0x00000010
SFGAO_CANDELETE    =     0x00000020
DROPEFFECT_COPY	 = 1
DROPEFFECT_MOVE	= 2
DROPEFFECT_LINK	= 4
SFGAO_VALIDATE = 0x01000000