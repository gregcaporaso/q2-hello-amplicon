# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = ("A template QIIME 2 plugin.")

setup(
    name="q2-hello-amplicon",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="A QIIME 2 Plugin Developer",
    author_email="q2-dev@example.com",
    description=description,
    url="https://example.com",
    entry_points={
        "qiime2.plugins": [
            "q2_hello_amplicon="
            "q2_hello_amplicon"
            ".plugin_setup:plugin"]
    },
    package_data={
        "q2_hello_amplicon": ["citations.bib"],
        "q2_hello_amplicon.tests": ["data/*"],
    },
    zip_safe=False,
)
