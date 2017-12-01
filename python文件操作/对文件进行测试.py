# 将导入脚本文件所在文件夹下的所有测试文件（以test结尾的脚本文件0，并进行测试。
import sys, os, re, unittest

def regressionTest():
	path = os.path.abspath(sys.argv[0])
	files = os.listdir(path)
	print(file)
	test = re.compile('test\.py$', re.IGNORECASE)
	files = filter(tese.serach, files)
	print(files)
	filenametoModulename = lambda f: os.path.spilttext(f)[0]
	print(filenametoModulename)

	modulesname = map(filenametoModulename, files)
	print(modulesname)

	modules = map(___import__, modulesname)

	load = unittest.defaultTestLoader.loadTestsFromModule

	return unittest.TestSuite(map(load, modules))


if __name__ == '__main__':
	unittest.main(defaultTest='regressionTest')
