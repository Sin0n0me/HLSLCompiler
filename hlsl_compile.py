import glob
import os
import subprocess

FXC_PATH = 'C:/Program Files (x86)/Windows Kits/10/bin/10.0.22621.0/x64'


def main():
    hlsl_files = glob.glob('*/**/*.hlsl', recursive=True)
    print(hlsl_files)

    for hlsl_file in hlsl_files:
        hlsl_file = hlsl_file.replace('\\', '/')
        hlsl_directory = os.path.dirname(hlsl_file)
        hlsl_file_name = os.path.basename(hlsl_file).split('.')[0]
        prefix = hlsl_file_name[:2].upper()

        shader_type = ''
        if prefix == 'VS':
            shader_type = 'vs_5_0'
        if prefix == 'PS':
            shader_type = 'ps_5_0'
        if prefix == 'TS':
            shader_type = 'tx_1_0'
        if prefix == 'GS':
            shader_type = 'gs_5_0'
        if prefix == 'HS':
            shader_type = 'hs_5_0'
        if prefix == 'CS':
            shader_type = 'cs_5_0'

        if shader_type == '':
            continue

        try:
            command = [
                f'{FXC_PATH}/fxc.exe',
                '/E', 'main',
                '/T', shader_type,
                '/Fh', f'{hlsl_directory}/{hlsl_file_name}.h',
                hlsl_file
            ]
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(e)


if __name__ == '__main__':
    main()
