from conans import ConanFile, tools, AutoToolsBuildEnvironment


class LibalsaConan(ConanFile):
    name = "libalsa"
    version = "1.1.5"
    license = "LGPL"
    url = "https://github.com/conan-community/conan-libalsa"
    description = "Library of ALSA: The Advanced Linux Sound Architecture, that provides audio " \
                  "and MIDI functionality to the Linux operating system"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build = "missing"

    def configure(self):
        if self.settings.os != "Linux":
            raise Exception("Only Linux supported")

    def source(self):
        self.run("git clone git://git.alsa-project.org/alsa-lib.git")
        self.run("cd alsa-lib && git checkout v%s" % self.version)

    def build(self):
        ab = AutoToolsBuildEnvironment(self)
        with tools.environment_append(ab.vars):
            with tools.chdir("alsa-lib"):
                self.run('./gitcompile --prefix="%s"' % self.package_folder)
                self.run("make install")

    def package_info(self):
        self.cpp_info.libs = ["asound"]
