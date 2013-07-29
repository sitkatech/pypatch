pypatch
=======

Automatically apply patches to third-party libraries as part of your build.

PyPatch is a command wrapper based around Anatoly Techtonik's patch.py utility. PyPatch allows you to patch python
libraries using a unified diff file. Specifically, PyPatch is meant to be used in automatic build processes where you
have a 3rd party library that needs to be patched when being deployed. Instead of maintaining your own separate version
of the library, you can just issue your patch during the build process.

Usage:
    pypatch apply [libarary.package] custom_diff.patch

As a part of the work flow:
    pip install django
    pip install pypatch
    pypatch apply django.contrib.auth c:\project\patches\my_auth_fix.patch

How it works:
    Pypatch applies patches to files relative to the root directory of the named package. So it does have to be
    installed into the target environment. This can be managed using

    For example, if the django package was installed to:
        "C:\Python27\Lib\site-packages\django"

    and you needed to patch the auth contrib package (django.contrib.auth), your command might look like
        "pypatch apply django.contrib.auth c:\project\patches\my_auth_fix.patch"

    and the files named in the my_auth_fix.patch diff would use relative pathing from the package directory:
        --- models.py	2013-05-06 15:12:14.212220100 -0700
        +++ models.py	2013-05-06 14:36:20.535220100 -0700

    If you used
        "pypatch apply django.contrib c:\project\patches\my_auth_fix.patch"

    instead, your diff patch would read
        --- auth/models.py	2013-05-06 15:12:14.212220100 -0700
        +++ auth/models.py	2013-05-06 14:36:20.535220100 -0700

Information on the Unified Diff format can be found at
    https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html#Unified-Format