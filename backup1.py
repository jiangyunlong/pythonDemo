import os
import time

source = 'C:\\Users\\Long\\Desktop\\asiainfo\\nh'

targetDir = 'C:\\Users\\Long\\Desktop\\asiainfo\\bak'

target = targetDir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'

if not os.path.exists(targetDir):
    os.mkdir(targetDir)

#zipCommand = 'zip -r {0} {1}'.format(target, ' '.join(source))
zipCommand = ('rar a "%s" "%s"'%(target,''.join(source)))

print('Zip command is:')
print(zipCommand)
print('Running:')

if os.system(zipCommand) == 0:
    print('Successful backup to', target)
else:
    print('backup failed')