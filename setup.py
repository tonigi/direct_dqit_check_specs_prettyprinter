from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='direct_check_specs_prettyprinter_py',
      version='0.2',
      description='Prettyprinter for DQIT DIRECT error-checking specifications',
      author='Toni Giorgino',
      author_email='toni.giorgino@isib.cnr.it',
      license='GPL',
      packages=['direct_check_specs_prettyprinter_py'],
      scripts=['bin/prettyprinter.py'],
      install_requires=[
          'Jinja2',
          'xlrd'
      ],
      )

#      zip_safe=False,
#      include_package_data=True
