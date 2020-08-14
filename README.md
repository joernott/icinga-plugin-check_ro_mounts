# nagios-plugin-check_ro_mount
This plugin checks the mount table for read-only mounts.

Originally found at https://exchange.nagios.org/directory/Plugins/Operating-Systems/Linux/check_ro_mounts/details,
this check reports read only mounts. I created this repository, because I needed to patch the path to run on 64bit 
RHEL 7. This also allows me to use tags for easier versioning and RPM building. 

## License
GPL v2 or later, Copyright (c) 2008 Valentin Vidic

## Usage
```
  check_ro_mounts [-m mtab] [-p path] [-x path] [-X type]

Options:
 -h, --help
    Print detailed help screen
 -m, --mtab=FILE
    Use this mtab instead (default is /proc/mounts)
 -p, --path=PATH, --partition=PARTITION
    Glob pattern of path or partition to check (may be repeated)
 -x, --exclude=PATH <STRING>
    Glob pattern of path or partition to ignore (only works if -p unspecified)
 -X, --exclude-type=TYPE <STRING>
    Ignore all filesystems of indicated type (may be repeated)
```