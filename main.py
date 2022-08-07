from crud import CRUDCategory

category = CRUDCategory.get(category_id=1)
print(category)
category.name = 'Еда'
CRUDCategory.update(category=category)
print(CRUDCategory.get(category_id=1))


#CRUDCategory.add(name="Стеки", parent_id=1)
#CRUDCategory.add(name="Ролы", parent_id=2)
#for category in CRUDCategory.get_all():
#    print(category.name)
#    print(category.__dict__)


