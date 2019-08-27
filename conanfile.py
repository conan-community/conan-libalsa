# -*- coding: utf-8 -*-
from conans import ConanFile, tools, AutoToolsBuildEnvironment
from conans.errors import ConanInvalidConfiguration
import os


class LibalsaConan(ConanFile):
    name = "libalsa"
    version = "1.1.9"
    license = "LGPL-2.1"
    url = "https://github.com/conan-community/conan-libalsa"
    homepage = "https://github.com/alsa-project/alsa-lib"
    author = "Conan Community"
    topics = ("conan", "libalsa", "alsa", "sound", "audio", "midi")
    description = "Library of ALSA: The Advanced Linux Sound Architecture, that provides audio " \
                  "and MIDI functionality to the Linux operating system"
    options = {"shared": [True, False], "fPIC": [True, False], "disable_python": [True, False]}
    default_options = {'shared': False, 'fPIC': True, 'disable_python': True}
    settings = "os", "compiler", "build_type", "arch"
    _autotools = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("Only Linux supported")
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def source(self):
        sha256 = "be3443c69dd2cb86e751c0abaa4b74343c75db28ef13d11d19a3130a5b0ff78d"
        tools.get("{}/archive/v{}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        os.rename("alsa-lib-{}".format(self.version), self._source_subfolder)

    def _configure_autotools(self):
        if not self._autotools:
            self._autotools = AutoToolsBuildEnvironment(self)
            with tools.environment_append(self._autotools.vars):
                self.run("touch ltconfig")
                self.run("libtoolize --force --copy --automake")
                self.run("aclocal $ACLOCAL_FLAGS")
                self.run("autoheader")
                self.run("automake --foreign --copy --add-missing")
                self.run("touch depcomp")
                self.run("autoconf")

            args = ["--enable-static=yes", "--enable-shared=no"] \
                    if not self.options.shared else ["--enable-static=no", "--enable-shared=yes"]
            if self.options.disable_python:
                args.append("--disable-python")
            self._autotools.configure(args=args)
        return self._autotools

    def build(self):
        with tools.chdir(self._source_subfolder):
            autotools = self._configure_autotools()
            autotools.make()

    def package(self):
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)
        with tools.chdir(self._source_subfolder):
            autotools = self._configure_autotools()
            autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["asound", "dl", "m", "rt", "pthread"]
        self.env_info.ALSA_CONFIG_DIR = os.path.join(self.package_folder, "share", "alsa")
