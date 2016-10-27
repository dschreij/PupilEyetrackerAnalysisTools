#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of fileinspector.

fileinspector is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fileinspector is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fileinspector.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup
import pupiltools

setup(
	name='pupiltools',
	version=pupiltools.__version__,
	description='Analysis tools for the pupil eyetracker',
	author='Daniel Schreij',
	author_email='dschreij@gmail.com',
	url='https://github.com/dschreij/PupilEyetrackerAnalysisTools',
	packages=['pupiltools'],
	classifiers=[
		'Intended Audience :: Developers',
		'Topic :: Desktop Environment',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
	install_requires=[
		'pandas',
		'statsmodels',
		'numpy',
		'scipy',
		'matplotlib',
		'six',
	],
	include_package_data=True,
)
