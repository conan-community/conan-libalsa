# conan-libalsa

![conan-libalsa image](/conan-libalsa.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/libalsa%3Aconan/images/download.svg?version=0.1-p0%3Astable)](https://bintray.com/conan-community/conan/libalsa%3Aconan/0.1-p0%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-libalsa.svg?branch=stable%2F0.1-p0)](https://travis-ci.org/conan-community/conan-libalsa)

[Conan.io](https://conan.io) package for [libalsa](https://www.alsa-project.org) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/libalsa%3Aconan).

## Basic setup

    $ conan install libalsa/1.1.5@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    libalsa/1.1.5@conan/stable

    [generators]
    txt
    cmake

## License

Current repo is [MIT License](LICENSE)
Check the specific license for the library being packaged.