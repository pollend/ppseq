from setuptools import Extension
from setuptools import setup




setup (name = 'ppseq',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules= [
         Extension('ppseq',['seq/module.go'])
       ],
       build_golang={'root': 'github.com/pollend/ppseq'}
       )
if __name__ == '__main__':
       pass