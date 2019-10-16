# -*- mode: python -*-

block_cipher = None


a = Analysis(['MAPIR_Camera_Control.py'],
             pathex=['C:\\Users\\Software\\Desktop\\GITHUB\\MAPIR_Camera_Control',
             'C:\\Program Files (x86)\\Windows Kits\\10\Redist\\10.0.18362.0\\ucrt\\DLLs\\x64',
             'C:\\Users\\Software\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\osgeo'],
             binaries=[('FreeImage.dll', '.'), ('FreeImagePlus.dll', '.'), ('opencv_aruco320.dll', '.'), ('opencv_aruco320d.dll', '.'), ('opencv_calib3d320.dll', '.'),
             ('opencv_calib3d320.dll', '.'),
             ('opencv_core320.dll', '.'),
             ('opencv_core320d.dll', '.'),
             ('opencv_features2d320.dll', '.'),
             ('opencv_flann320.dll', '.'),
             ('opencv_imgcodecs320.dll', '.'),
             ('opencv_imgproc320.dll', '.')],

             datas=[('exiftool.exe', '.'),
             ('dcraw.exe', '.'),
             ('FiducialFinder.exe', '.'),
             ('Mapir_Converter.exe', '.'),
             ('instring.txt', '.'),
             ('calib.txt', '.'),
             ('MAPIR_Processing_dockwidget_base.ui', '.'),
             ('MAPIR_Processing_dockwidget_CAN.ui', '.'),
             ('MAPIR_Processing_dockwidget_modal.ui', '.'),
             ('MAPIR_Processing_dockwidget_time.ui', '.'),
             ('MAPIR_Processing_dockwidget_delete.ui', '.'),
             ('MAPIR_Processing_dockwidget_transfer.ui', '.'),
             ('MAPIR_Processing_dockwidget_LUT.ui', '.'),
             ('MAPIR_Processing_dockwidget_raster.ui', '.'),
             ('MAPIR_Processing_dockwidget_Viewer_Save.ui', '.'),
             ('MAPIR_Processing_dockwidget_A_Exposure.ui', '.'),
             ('MAPIR_Processing_dockwidget_M_Exposure.ui', '.'),
             ('MAPIR_Processing_dockwidget_vignette.ui', '.'),
             ('MAPIR_Processing_dockwidget_BandOrder.ui', '.'),
             ('MAPIR_Processing_dockwidget_Advanced.ui', '.'),
             ('MAPIR_Processing_dockwidget_matrix.ui', '.'),
             ('vig_405.txt', '.'),
             ('vig_450.txt', '.'),
             ('vig_490.txt', '.'),
             ('vig_518.txt', '.'),
             ('vig_550.txt', '.'),
             ('vig_590.txt', '.'),
             ('vig_615.txt', '.'),
             ('vig_632.txt', '.'),
             ('vig_685.txt', '.'),
             ('vig_725.txt', '.'),
             ('vig_780.txt', '.'),
             ('vig_808.txt', '.'),
             ('vig_850.txt', '.'),
             ('vig_880.txt', '.'),
             ('vig_940.txt', '.'),
             ('vig_RGB_8.25_1.txt', '.'),
             ('vig_RGB_8.25_2.txt', '.'),
             ('vig_RGB_8.25_3.txt', '.'),
             ('vig_RGB_3.37_1.txt', '.'),
             ('vig_RGB_3.37_2.txt', '.'),
             ('vig_RGB_3.37_3.txt', '.'),
             ('vig_RGN_8.25_1.txt', '.'),
             ('vig_RGN_8.25_2.txt', '.'),
             ('vig_RGN_8.25_3.txt', '.'),
             ('vig_RGN_3.37_1.txt', '.'),
             ('vig_RGN_3.37_2.txt', '.'),
             ('vig_RGN_3.37_3.txt', '.'),
             ('Flat_Field_Poly_Coeffs.json', '.'),
             ('Dark_Frame_Values.json', '.'),
             ('msvcp100.dll', '.'),
             ('msvcr100.dll', '.'),
             ('corn_logo_color_ico.ico', '.'),
             ('msvcr100_clr0400.dll', '.'),
             ('lut_legend.jpg', '.'),
             ('lut_legend_rgb.jpg', '.'),
             ('lut_red-to-green.jpg', '.'),
             ('ndvi_400px.jpg', '.'),
             ('mapir.config', '.'),
             ('mapir_kernel.camerarig', '.'),
             ('template.kernelconfig', '.'),
             ('dark.qss', '.'),
             ('breeze_resouces.py','.'),
             ('breeze.qrc','.'),
             ('dark\*.svg', 'dark') ],

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
          Tree('C:\\Users\\Software\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\osgeo'),
          name='MAPIR_Camera_Control',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='C:\\Users\\Software\\Desktop\\GITHUB\\MAPIR_Camera_Control\\corn_logo_color_ico.ico')
