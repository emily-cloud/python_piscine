def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if(obj_type is str):
        print(f"{object} is in the kitchen : {obj_type}")
    elif(obj_type is int):
        print("Type not found")
    else:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    return 42