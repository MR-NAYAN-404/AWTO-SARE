import os,platform,time,requests

bitt=platform.architecture()[0]

if bitt=="64bit":
    ip = requests.get("https://api.ipify.org").text
    os.system('clear');print('\x1b[1;92m[!] Your Device Supported This Tool🥰');time.sleep(1);print('\n\n\x1b[1;92m[!] Your Ip : '+ip);time.sleep(1);print('\n\n\x1b[1;92m[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(5)
    import nsare

else:

    print('\nYOUR DEVICE 32 BIT NOT SUPPORT')
