PyPatch
=======

Automatically apply patches to third-party libraries as part of your build.

Now and again, a specific fix is needed for a python package that isn't available from the vendor/community.
This project was created to allow a way for us to patch specific python modules during the build process.

PyPatch is a command wrapper based around Anatoly Techtonik's patch.py utility. PyPatch allows you to patch python
libraries using a unified diff file. Specifically, PyPatch is meant to be used in automatic build processes where you
have a 3rd party library that needs to be patched when being deployed. Instead of maintaining your own separate version
of the library, you can just issue your patch during the build process.

Usage
---
```pypatch apply custom_diff.patch [libarary.package]```

As a part of the work flow:

```c:\project\pip install django
   c:\project\pip install pypatch
   c:\project\pypatch apply c:\project\patches\my_auth_fix.patch django.contrib.auth```

How it works
------------
PyPatch applies patches to files relative to the root directory of the named package. So it does have to be installed into the target environment.

For example, if the django package was installed to "C:\Python27\Lib\site-packages\django" and you needed to patch the auth contrib package (django.contrib.auth), your command might look like

```pypatch apply c:\project\patches\my_auth_fix.patch django.contrib.auth"```

and the files named in my_auth_fix.patch would use relative pathing from the package directory:

```
--- models.py    2013-05-06 15:12:14.212220100 -0700
+++ models.py	2013-05-06 14:36:20.535220100 -0700
```

If you used

```pypatch apply c:\project\patches\my_auth_fix.patch django.contrib```

instead, your diff patch would read
```
--- auth/models.py	2013-05-06 15:12:14.212220100 -0700
+++ auth/models.py	2013-05-06 14:36:20.535220100 -0700
```

Build
-----
To build the distributable python package, run 'sdist' from the Project Root Directory.
Recommended: setting the output directory to our Libraries folder

```sdist --dist-dir="C:\outputdir"```

This will build the zipped python package that can be installed via pip or easy_install

Other
-----
Information on the Unified Diff format can be found at
    https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html#Unified-Format
