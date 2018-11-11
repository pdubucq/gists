# -*- coding: utf-8 -*-
import pyrobocopy, os, time
t = time.time()
#
# Institutsarbeit
os.system('pyrobocopy.py D:/Dropbox/Institutsarbeit e:\Uni\Institutsarbeit\ -s -c -p > Institutsarbeit.log')
print 'Institutsarbeit done. Elapsed: %.1f minutes' % ((time.time() - t)/60)
# Dissertation
os.system('pyrobocopy.py D:/Dropbox/Dissertation e:\Uni\Dissertation\ -s -c -p > Dissertation.log')
print 'Dissertation done. Elapsed: %.1f minutes' % ((time.time() - t)/60)
# TEEsatz ohne purge, weil die Ergebnisse nicht mehr in der Cloud sind, aber sehr wohl auf E!
os.system('pyrobocopy.py d:\Transient\TEEsatz e:\Uni\TransiEnt\TEEsatz\ -s -c > TEEsatz.log')
print 'TEEsatz done. Elapsed: %.1f minutes' % ((time.time() - t)/60)
# Unversioniert
os.system('pyrobocopy.py d:\Transient\Unversioniert e:\Uni\TransiEnt\Unversioniert\ -s -c -p > Unversioniert.log')
print 'Unversioniert done. Elapsed: %.1f minutes' % ((time.time() - t)/60)
# transientee-sources (use git instead!)
os.system('pyrobocopy.py d:/Transient/Git/transientee-sources e:\Uni\TransiEnt\Git\transientee-sources/ -s -c -p > SourcesGit.log')
print 'SourcesGit done. Elapsed: %.1f minutes' % ((time.time() - t)/60)
# TransiEnt sources