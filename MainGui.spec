# -*- mode: python -*-

block_cipher = None


a = Analysis(['MainGui.py', 'MyGenWindow.py', 'MyPlotWindow.py', 'MysqlCon.py', 'OnlyTest.py', 'PyGenerateData.py'],
             pathex=['/Users/hepeng/workspace/python/homework'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MainGui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='MainGui.app',
             icon=None,
             bundle_identifier=None)
