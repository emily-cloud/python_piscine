def NULL_not_found(object: any) -> int:
	value_type = type(object)

	if object is None:
		print(f"Nothing: {object} {value_type}")
		return 0
	elif value_type is float and object != object:
		print(f"Cheese: {object} {value_type}")
		return 0
	elif value_type is int:
		print(f"Zero: {object} {value_type}")
		return 0
	elif value_type is str and object == "":
		print(f"Empty: {object} {value_type}")
		return 0
	elif value_type is bool:
		print(f"Fake: {object} {value_type}")
		return 0
	return 1
