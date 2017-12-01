
# BaseException作为所有异常的母亲
# 同时try-except语句还可以加上else语句
# 和正常的执行没有什么不同，也就是在try范围中没有异常被检测到时，执行else子句。

# finally子句是无论异常是否发生，是否捕捉都会的执行一段代码。

# 触发异常
# raise [SomeException [, arges [, trackback]]]
# 第一个参数，SomeException，是触发异常的名字。如果有，它必须是一个字符串，类或实例.
# 如果有其他参数(arg 或 traceback)就必须提供SomeException.

# 第二个符号为可选的 args ，来传给异常。
# 这可以是一个单独的对象也可以是一个对象的元组。
# 如果args原本就是元组，那么就将其传给异常区处理；
# 如果args是一个单独的对象，就生成只有一个元素的元组。
# 大多数情况下，单一的字符串用来指示错误的原因。
# 如果传的是元组，通常的组成是一个错误字符串，一个错误编号，可能还有一个错误的地址，比如文件。

# 最后一个参数，traceback，也是可选的。
# 如果有的话，是新生成的一个用于异常-正常话的追踪对象。
# 当你想重新引发异常时，第三个参数很有用。

# 断言
# 断言是一句必须等价于布尔真的判定；此外发生发生异常也意味着表达式为假。
# 断言语句语法：

# assert expression[, arguments]
# 断言成功不采取任何措施，否则处罚AssertionError异常。

def safe_float(obj):
	try:
		reval = float(obj)

	except ValueError:
		reval = 'could not convert non-number to float'
	except TypeError:
		reval = 'object type cound not convert to float'

	except (ValueError, TypeError):
		reval = 'argument must be number or numeric string'


	# 并存储为类实例的属性。上面这样的用法，reason将会是Exception类的实例。
	except Exception, e:
		print('将异常种类存储在e中，异常参数自身会组成一个元组')

	return reval

print(safe_float(['xyz',213]))