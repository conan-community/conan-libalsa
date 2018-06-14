from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class LibalsaConan(ConanFile):
    name = "libalsa"
    version = "1.1.5"
    license = "LGPL"
    url = "https://github.com/conan-community/conan-libalsa"
    description = "Library of ALSA: The Advanced Linux Sound Architecture, that provides audio " \
                  "and MIDI functionality to the Linux operating system"
    options = {"shared": [True, False], "disable_python": [True, False]}
    default_options = "shared=False", "disable_python=False"
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"

    def configure(self):
        if self.settings.os != "Linux":
            raise Exception("Only Linux supported")

    def source(self):
        self.run("git clone git://git.alsa-project.org/alsa-lib.git")
        self.run("cd alsa-lib && git checkout v%s" % self.version)

    def build(self):
        ab = AutoToolsBuildEnvironment(self)
        with tools.environment_append(ab.vars):
            with tools.chdir(os.path.join(self.source_folder, "alsa-lib")):
                args = ["--enable-static=yes", "--enable-shared=no"] \
                    if not self.options.shared else ["--enable-static=no", "--enable-shared=yes"]
                python = "--disable-python" if self.options.disable_python else ""
                self.run("touch ltconfig")
                self.run("libtoolize --force --copy --automake")
                self.run("aclocal $ACLOCAL_FLAGS")
                self.run("autoheader")
                self.run("automake --foreign --copy --add-missing")
                self.run("touch depcomp")
                self.run("autoconf")
                if python:
                    args.append(python)
                args.append('--prefix=%s' % self.package_folder)
                ab.configure(args=args)
                self.run("make install")

    def package(self):
        self.copy("*LICENSE*", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = ["asound", "dl", "pthread"]
        self.env_info.ALSA_CONFIG_DIR = os.path.join(self.package_folder, "share", "alsa")
