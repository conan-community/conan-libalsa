# conan-libalsa

![conan-libalsa image](conan_libalsa.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/libalsa%3Aconan/images/download.svg?version=1.1.5%3Astable)](https://bintray.com/conan-community/conan/libalsa%3Aconan/1.1.5%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-libalsa.svg?branch=release%2F1.1.5)](https://travis-ci.org/conan-community/conan-libalsa)

[Conan.io](https://conan.io) package for [libalsa](https://www.alsa-project.org) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/libalsa%3Aconan).

## Basic setup

    $ conan install libalsa/1.1.5@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    libalsa/1.1.5@conan/stable

    [generators]
    cmake
    
    [imports]
    share, alsa/alsa.conf -> ./bin
    
 
The libalsa need to be able to locate the ``alsa.conf`` file.
With the above ``[imports]`` statement we are copying the ``alsa.conf`` to a local folder.
The location can be specified with any of these environment variables:

- ALSA_CONFIG_PATH: Absolute path to the ``alsa.conf`` 
- ALSA_CONFIG_DIR: Directory where the ``alsa.conf`` is.


**Example:**

    conan install .
    //build your project in bin/ folder
    cd bin && ALSA_CONFIG_DIR=$(pwd) ./myproject
    


## License

Current repo is [MIT License](LICENSE)
Check the specific license for the library being packaged.