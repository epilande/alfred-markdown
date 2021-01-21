import os
import subprocess

clip0 = os.environ['clip0']
clip1 = os.environ['clip1']
clip2 = os.environ['clip2']
clip3 = os.environ['clip3']
clip4 = os.environ['clip4']
clip5 = os.environ['clip5']
clip6 = os.environ['clip6']
clip7 = os.environ['clip7']
clip8 = os.environ['clip8']
clip9 = os.environ['clip9']

result = subprocess.run(['osascript', '-e',
                         'if application "Google Chrome" is running then tell application "Google Chrome" to return URL of active tab of front window'
                         ], stdout=subprocess.PIPE)
activeTabUrl = result.stdout.decode('utf-8')

clipboard = filter(None, [
    activeTabUrl,
    clip0,
    clip1,
    clip2,
    clip3,
    clip4,
    clip5,
    clip6,
    clip7,
    clip8,
    clip9,
])
