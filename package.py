name = "libraw"

authors = [
    "LibRaw LLC",
]

version = "0.20.2"

description = \
    """
    Library for reading and processing of RAW digicam images
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "lcms",
    "libjpeg",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

tools = [
]

uuid = "repository.LibRaw"

build_system = "cmake"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.LIBRAW_ROOT = "{root}"
    env.LIBRAW_LOCATION = "{root}"
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
