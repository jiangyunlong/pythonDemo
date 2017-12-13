import os
import time

source = 'C:\\Users\\Long\\Desktop\\asiainfo\\nh'

targetDir = 'C:\\Users\\Long\\Desktop\\asiainfo\\bak'

today = targetDir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.rar'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

#zipCommand = 'zip -r {0} {1}'.format(target, ' '.join(source))
zipCommand = ('rar a "%s" "%s"'%(target,''.join(source)))

print('Zip command is:')
print(zipCommand)
print('Running:')

if os.system(zipCommand) == 0:
    print('Successful backup to', target)
else:
    print('backup failed')