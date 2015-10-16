import codecs
from setuptools import setup, find_packages

VERSION = '0.0.0'

entry_points = {
	'console_scripts': [
	],
}

TESTS_REQUIRE = [
	'nose',
	'nose-timer',
	'nose-pudb',
	'nose-progressive',
	'nose2[coverage_plugin]',
	'pyhamcrest',
	'zope.testing',
	'nti.nose_traceback_info',
	'nti.testing'
]

setup(
	name='nti.contentindexing',
	version=VERSION,
	author='Jason Madden',
	author_email='jason@nextthought.com',
	description="NTI Content Indexing Interfaces",
	long_description=codecs.open('README.rst', encoding='utf-8').read(),
	license='Proprietary',
	keywords='Content Indexing Interfaces',
	classifiers=[
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: Implementation :: CPython'
	],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	namespace_packages=['nti'],
	tests_require=TESTS_REQUIRE,
	install_requires=[
		'setuptools',
		'six',
		'Whoosh',
		'zope.component',
		'zope.interface',
		'zope.schema',
		'zope.security',
		'nti.common',
		'nti.contentfragments',
		'nti.contentprocessing',
		'nti.schema'
	],
	extras_require={
		'test': TESTS_REQUIRE,
	},
	dependency_links=[],
	entry_points=entry_points
)
