import os
import time

source = 'C:\\Users\\Long\\Desktop\\asiainfo\\nh'

targetDir = 'C:\\Users\\Long\\Desktop\\asiainfo\\bak'

today = targetDir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.rar'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zipCommand = 'rar a {0} {1}'.format(target, source)
#zipCommand = ('rar a "%s" "%s"'%(target,source))

print('Zip command is:')
print(zipCommand)
print('Running:')

if os.system(zipCommand) == 0:
    print('Successful backup to', target)
else:
    print('backup failed')