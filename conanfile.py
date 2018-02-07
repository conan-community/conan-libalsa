from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment


class LibalsaConan(ConanFile):
    name = "libalsa"
    version = "1.1.5"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libalsa here>"
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
