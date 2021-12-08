import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlog",
    version="0.0.1",
    author="kent taguba",
    author_email="ktag.dev@gmail.com",
    description="Journal/Logging utility that I personally wanted to have in any given linux terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktag0629/jlogger",
    project_urls={
        "Bug Tracker": "https://github.com/ktag0629/jlogger/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],

    packages=['jlog', 'jlog.utils', 'tests', 'config'],
    test_suite='tests',
    include_package_data=True,
    scripts=['jlog/jlog']
)

