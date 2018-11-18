from setuptools import setup, find_packages

setup(name='ds-image',
      version='0.0.1',
      description='A solver of ds-code-interview program b',
      python_requires='>=3.6.5',
      url='https://bitbucket.org/uzabase/ds-image',
      author='Nakamura, Ryotaro',
      author_email='ryotaro.nakamura@uzabase.com',
      license='UZABASE Inc.',
      classifiers=['Programming Language :: Python :: 3.6'],
      packages=find_packages(),
      install_requires=['tensorflow', 'scikit-learn', 'pillow', 'pandas'],
      extras_require={'dev': ['ipython', 'pytest-watch', 'pylint', 'autopep8', 'pytest-env', 'pytest']},
      entry_points={'console_scripts': ['ds-image=ds_image:main']})