from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"])
    builder.add_common_builds(shared_option_name="libalsa:shared", pure_c=True)
    builder.run()
