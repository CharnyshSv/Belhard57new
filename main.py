from crud import CRUDCategory

#category = CRUDCategory.get(category_id=1)
#print(category)
#category.name = 'Еда'
#CRUDCategory.update(category=category)
#print(CRUDCategory.get(category_id=1))


#CRUDCategory.add(name="Стеки", parent_id=1)
#CRUDCategory.add(name="Ролы", parent_id=2)
#for category in CRUDCategory.get_all():
#    print(category.name)
#    print(category.__dict__)

#async def main():
#    res = await CRUDArticle.get_all()
#    print(res)
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#asyncio.run(main())
import asyncio


async def main():
    res = await CRUDCategory.add
    print(res)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

