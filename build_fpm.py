#!/usr/bin/env python3

import os
import sys

# list of all platforms to build
# package type, distribution, arch
packages = [
    ["pacman", None,"x86_64"], 
    ["rpm","el7.5","x86_64"], 
    ["rpm","el7.6","x86_64"], 
    ["rpm","el7.7","x86_64"], 
    ["rpm","el8.0","x86_64"], 
    ["rpm","fc31","x86_64"], 
    ["rpm","fc32","x86_64"], 
    ["rpm", None,"x86_64"],
    ["deb", "stable", "amd64"]
]

# package properties
name = "googler"
maintainer = "Arun Prakash Jana <engineerarun@gmail.com>"
url = "https://github.com/jarun/googler"
license = "GPLv3"
description = "Google from the command-line."
version = sys.argv[1]
print(version)

# make temp dist dir
os.system("mkdir dist-fpm")

# zip manual binaries
os.system("gzip -9nc googler.1 > googler.1.gz")

for package in packages:
    target = package[0]
    dist = package[1]
    arch = package[2]

    fpm_command = "fpm \
        -t "+ target+ "\
        -n " + name +  "\
        -m \"" + maintainer + "\" \
        --url " + url + "\
        --license " + license + "\
        -d python3 \
        -v " + version + "\
        --description \"" + description + "\" \
        -a " + arch

    if (target == "rpm"):
        fpm_command += " --rpm-os linux"
    
    if (dist != None):
        if (target == "rpm"):
            fpm_command += " --rpm-dist " + dist
        elif (target == "deb"):
            fpm_command += " --deb-dist " + dist


    fpm_command += " -s dir ./googler=/usr/bin/ ./googler.1.gz=/usr/share/man/man1/ ./README.md=/usr/share/doc/googler/"

    print(fpm_command)
    os.system(fpm_command)

# move every package to dist
os.system("mv " + name + "-" + version + "* dist-fpm/")
os.system("mv " + name + "_" + version + "* dist-fpm/")

# remove zipped manual file
os.system("rm googler.1.gz")